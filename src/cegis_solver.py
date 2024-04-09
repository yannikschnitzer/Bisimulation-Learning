"""
 Main Classes for CEGIS Procedure of Bisimulation Learning. Contains Learner, Verifier and also one-shot solving without learning.
"""

import time
from utils import *
from experiment import Experiment
from visualization import *
from z3 import *
from conditional_termination_succ_trees import *
import matplotlib.pyplot as plt

__author__ = "Yannik Schnitzer"
__copyright__ = "Copyright 2024, Yannik Schnitzer"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "yannik.schnitzer@cs.ox.ac.uk"
__status__ = "Experimental - Artifact Evaluation"


def setup_smt_parameters(num_params, num_coefficients, num_partitions, dim):
    """
        Function returns the requested number of SMT parameters.
        Returns:
            - m: State variable of specified dimension
            - p,q: Abstract state variables
            - partitions: List of classes, i.e., abstract states, numbered from 0 to num_partitions - 1
            - adjacency_params: Booleans of the form a_i_j, for an abstract edge between partitions i and j
            - model_params: Real valued coefficients and predicate parameters for the BDT classifier templates
            - rank_params: Real valued coefficients and constatns for the ranking function templates
    """
    m = [Int("m_%s" % i) for i in range(dim)]
    p = Int("p")
    q = Int("q")

    partitions = [IntVal(i) for i in range(num_partitions)]
    adjacency_params = [[Bool("a_%s_%s" % (i, j)) for j in range(len(partitions))] for i in range(len(partitions))]
    model_params = [Real("p_%s" % i) for i in range(num_params)] + [Real("a_%s" % i) for i in range(num_coefficients)]
    rank_params = [[Real("u_%s_%s" % (j, i)) for j in range(dim)] + [Real("c_%s" % i)] for i in range(num_partitions)]

    return partitions, adjacency_params, model_params, rank_params, m, p, q


class CEGIS_Solver:
    """
        CEGIS Solver for (stutter-insensitive) bisimulation learning with ranking functions.
    """
    def __init__(self, name = "CEGIS Solver"):
        self.name = name

    def solve_experiment(self, exp : Experiment, verbose = False):
        """
            One-shot solve a given experiment. 
            Returns:
                - bdt_params: Obtained parameters for the given BDT template
                - abs_trans: Obtained abstract transition matrix
                - rank_params: Obtained parameters for the given ranking function templates.
        """
        return self.solve(exp.classifier,
                exp.successor,
                exp.domain,
                exp.num_params,
                exp.num_coefficients,
                exp.num_partitions,
                exp.dim,
                exp.num_initial,
                verbose = verbose)

    def solve(self, classifier, successor, domain, num_params, num_coefficients, num_partitions, dim, num_initial = 10, verbose = False):
        # SMT Parameters
        partitions, adjacency_params, model_params, rank_params, m, p, q = setup_smt_parameters(num_params, num_coefficients, num_partitions, dim)

        self.num_partitions = len(partitions)
        # SMT Soler
        s = Solver()

        def classify(params, x):
            f, _ = classifier(params, x, num_params, partitions)
            return f

        self.init_adjacency(num_partitions, adjacency_params)
        mp, ap, rankp, ctxs = self.add_initial_samples(s, classify, successor, model_params, adjacency_params, rank_params, partitions, domain, p, q, dim, num = num_initial)
        mp, ap, rankp, ctxs = self.cegis_rank(s, ctxs, classify, successor, model_params, adjacency_params, rank_params, partitions, domain, m, p, q, verbose = verbose)

        return mp, ap, rankp
    
    def cegis_rank(self, s, ctxs, classify, successor, model_params, adjacency_params, rank_params, partitions, domain, m, p, q, num_it = 30, verbose = False):
        mp, ap, rankp = extract_learner(s, model_params, adjacency_params, rank_params, partitions, verbose)

        # Track intermediate results for analysis / plotting purposes
        mps = []
        aps = []
        rankps = []
        ctxsss = []

        num_partitons = len(partitions)

        verified = True
        for _ in range(num_it):
            s.push()
    
            ctxs_cond_1 = (self.ver_cond_1(classify, successor, mp, ap, domain, m, num_partitons))
            if verbose: print("Counterexamples Condition 1: ", ctxs_cond_1)
            if ctxs_cond_1 != None: 
                ctxs = self.learn_ctxs(s, ctxs, ctxs_cond_1, classify, successor, model_params, rank_params, domain, p, q, num_partitons)
                verified = False

            ctxs_cond_2 = (self.ver_cond_2(classify, successor, mp, ap, rankp, domain, m, num_partitons))
            if verbose: print("Counterexamples Condition 2: ", ctxs_cond_2)
            if ctxs_cond_2 != None: 
                ctxs = self.learn_ctxs(s, ctxs, ctxs_cond_2, classify, successor, model_params, rank_params, domain, p, q, num_partitons)
                verified = False

            if verified: break
            verified = True

            mp, ap, rankp = extract_learner(s, model_params, adjacency_params, rank_params, partitions, verbose)
            mps.append(mp)
            aps.append(ap)
            rankps.append(rankp)
            ctxsss.append(ctxs)
        return mp, ap, rankp, ctxs

    def add_initial_samples(self, s, classify, successor, model_params, adjacency_params, rank_params, partitions, domain, p, q, dim, num = 10, r = 100):
        """
            Add a specified number of randomly generated initial samples to the solver.
        """
        ctxs = generate_samples(num, dom =[[-r,r] for _ in range(dim)], dim = dim)
        self.conds_cegis_learner(s, ctxs, classify, successor, model_params, rank_params, domain, p, q, len(partitions))
        mp, ap, rankp = extract_learner(s, model_params, adjacency_params, rank_params, partitions)
        return mp, ap, rankp, ctxs

    def learn_ctxs(self, s, ctxs, new_ctxs, classify, successor, model_params, rank_params, domain, p, q, num_partitions):
        """
            Add new conditions for new counterexamples to the solver.
        """
        if new_ctxs == None: return ctxs
        ctxs = np.concatenate((ctxs, new_ctxs), axis = 0)
        self.conds_cegis_learner(s, new_ctxs, classify, successor, model_params, rank_params, domain, p, q, num_partitions)
        return ctxs

    def conds_cegis_learner(self, solver, ctxs, classify, successor, model_params, rank_params, domain, p , q, num_partitions):
        """
            Conditions 1 and 2 for the learner of (stutter-insensitive) bisimulation learning
        """
        for m in ctxs:
            succ = successor(m)
            classification = classify(model_params, m)
            class_succ = classify(model_params, succ)
            is_dom = domain(m)
            is_dom_succ = domain(succ)

            for p in range(num_partitions):
                rnk = self.get_rank(p, m, rank_params)
                rnk_succ = self.get_rank(p, succ, rank_params)
                for q in range(num_partitions):
                    adj_val = self.get_adjacency(p, q)
                    if (not p == q):
                        solver.add(
                            simplify(Implies(And(classification == p, 
                                                            class_succ == q, is_dom, is_dom_succ), 
                                                adj_val == 1))
                        )
                        solver.add(
                                simplify(
                                        Implies(And(adj_val == 1, classification == p, is_dom, is_dom_succ), 
                                            Or(class_succ == q,
                                                And(class_succ == p, rnk > rnk_succ))    
                                        ) 
                                )
                        )
    
    def eval(self, m, x):
        """
            Evaluate Z3 result
        """
        return m.evaluate(x) if not (m.evaluate(x) == x) else 0

    def ver_cond_1(self, classify, successor, model_params, adjacency_params, domain, m, num_partitions):
        """
            Verification of Condition 1. Check for counterexample state whose transition is not matched by an abstract transition.
        """
        s = Solver()
        
        succ = successor(m)
        classification = classify(model_params, m)
        class_succ = classify(model_params, succ)
        is_dom = domain(m)
        is_dom_succ = domain(succ)

        s.add(Or([simplify(Not(Implies(And(classification == p, 
                                                        class_succ == q, is_dom, is_dom_succ, (Not(p == q))), 
                                            adjacency_params[p][q] == True))) for p in range(num_partitions) for q in range(num_partitions)]))


        if s.check() == sat:
            mod = s.model()
            ctx = [[self.eval(mod,n) for n in m]]
            return ctx
        else:
            return None


    def ver_cond_2(self, classify, successor, model_params, adj_params, rank_params, domain, m, num_partitions):
        """
            Verification of Condition 2. Check for counterexample state who can not match the abstract transition of its assigned class.
        """
        s = Solver()
        
        succ = successor(m)
        classification = classify(model_params, m)
        class_succ = classify(model_params, succ)
        is_dom = domain(m)
        is_dom_succ = domain(succ)

        s.add(Or([simplify(Not(
                    Implies(And(adj_params[p][q] == True, classification == p, is_dom, is_dom_succ, Not(p == q)), 
                        Or(class_succ == q,
                            And(class_succ == p, self.get_rank(p, m, rank_params) > self.get_rank(p, succ, rank_params)))    
                    ))) for p in range(num_partitions) for q in range(num_partitions)]))

        if s.check() == sat:
            mod = s.model()
            ctx = [[self.eval(mod,n) for n in m]]
            return ctx
        else:
            return None



    def init_adjacency(self, num_partitions, adjacency_params):
        """
            Initialize adjacency parameters
        """
        self.adj_exprs = [[self.adjacency(adjacency_params,p,q) for q in range(num_partitions)] for p in range(num_partitions)]

    def generate_adjacency(self, p, q, i , j, params, mx):
        if i == mx and j == mx:
            return simplify(If(And(p == i, q == j),If(params[i][j],1,0),0))
        elif i <= mx and j < mx:
            return simplify(If(And(p == i, q == j), If(params[i][j],1,0), self.generate_adjacency(p,q,i,j+1,params,mx)))
        elif i < mx and j == mx:
            return simplify(If(And(p == i, q == j), If(params[i][j],1,0), self.generate_adjacency(p,q,i+1,0,params,mx)))

    def adjacency(self, params, p, q): 
        return self.generate_adjacency(p,q,0,0,params,self.num_partitions - 1)
    
    def get_rank(self, p, x, params):
        """
            Get instantiated linear ranking function for given parameters
        """
        return np.dot(params[p][:-1], x) + params[p][-1]

    def get_adjacency(self, p, q):
        """
            Get precomputed adjacency parameter
        """
        return self.adj_exprs[p][q]
                            

class One_Shot_Solver:
    """
        One-Shot SMT Solver for stutter-insensitive bisimulation conditions with ranking functions.
    """
    def __init__(self, name = "One-Shot Solver"):
        self.name = name

    def solve_experiment(self, exp : Experiment):
        """
            One-shot solve a given experiment. 
            Returns:
                - bdt_params: Obtained parameters for the given BDT template
                - abs_trans: Obtained abstract transition matrix
                - rank_params: Obtained parameters for the given ranking function templates.
        """
        return self.solve(exp.classifier,
              exp.successor,
              exp.domain,
              exp.num_params,
              exp.num_coefficients,
              exp.num_partitions,
              exp.dim)

    def solve(self, classifier, successor, domain, num_params, num_coefficients, num_partitions, dim):
        # SMT Parameters
        partitions, adjacency_params, model_params, rank_params, m, p, q = setup_smt_parameters(num_params, num_coefficients, num_partitions, dim)

        self.num_partitions = len(partitions)
        # SMT Soler
        s = Solver()

        def classify(params, x):
            f, _ = classifier(params, x, num_params, partitions)
            return f

        # Add Stutter-Insensitive Bisimulation conditions with ranking functions
        self.cond_1_one_shot(s, classify, successor, model_params, adjacency_params, domain, m, p, q)
        self.cond_2_one_shot(s, classify, successor, model_params, adjacency_params, rank_params, domain, m, p, q)

        mp, ap, rankp = extract_learner(s, model_params, adjacency_params, rank_params, partitions)
        return mp, ap, rankp

    def cond_1_one_shot(self, solver, classify, successor, model_params, adj_params, domain, m, p ,q):
        """
            Condition 1 of a stutter-insensitive bisimulation - Concrete transitions imply abstract transitions
        """
        solver.add(
            simplify(ForAll([*m,p,q], Implies(And(classify(model_params, m) == p, 
                                            classify(model_params, successor(m)) == q, domain(m), domain(successor(m)), (Not(p == q))), 
                                self.adjacency(adj_params, p, q) == 1)))
        )

    def cond_2_one_shot(self, solver, classify, successor, model_params, adj_params, rank_params, domain, m, p ,q):
        """
            Condition 2 of a stutter-insensitive bisimulation with ranking functions - abstract transitons imply concrete transition or intra-class ranking transition
        """
        solver.add(
                simplify(ForAll([*m,p,q], And(
                                    Implies(And(self.adjacency(adj_params, p ,q) == 1, Not(p == q),classify(model_params,m) == p, domain(m), domain(successor(m))), 
                                        Or(classify(model_params, successor(m)) == q,
                                            And(classify(model_params, successor(m)) == p, self.rank(p, m, rank_params) > self.rank(p, successor(m), rank_params)))    
                                    ) ,
                                    Implies(And(self.adjacency(adj_params, p ,q) == 1, (p == q)), 
                                        Implies(And(classify(model_params, m) == p, domain(m), domain(successor(m))), classify(model_params,successor(m)) == p)
                                        )
                                )
                        )
                )
        )

    def generate_adjacency(self, p, q, i , j, params, mx):
        if i == mx and j == mx:
            return simplify(If(And(p == i, q == j),If(params[i][j],1,0),0))
        elif i <= mx and j < mx:
            return simplify(If(And(p == i, q == j), If(params[i][j],1,0), self.generate_adjacency(p,q,i,j+1,params,mx)))
        elif i < mx and j == mx:
            return simplify(If(And(p == i, q == j), If(params[i][j],1,0), self.generate_adjacency(p,q,i+1,0,params,mx)))

    def adjacency(self, params, p, q): 
        return self.generate_adjacency(p,q,0,0,params,self.num_partitions - 1)
    
    def generate_rank(self, p, x, params, i):
        if i == len(params)-1: 
            return np.dot(params[i][:-1], x) + params[i][-1]
        return simplify(If(p == i, np.dot(params[i][:-1], x) + params[i][-1], self.generate_rank(p, x, params, i+1)))

    def rank(self, p, x, params):
        return self.generate_rank(p, x, params, 0)