"""
 Utility and helper functions.
"""

from experiment import *
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from z3 import *


__author__ = "Yannik Schnitzer"
__copyright__ = "Copyright 2024, Yannik Schnitzer"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "yannik.schnitzer@cs.ox.ac.uk"
__status__ = "Experimental - Artifact Evaluation"

seed = 55 # Random seed for random initial samples, 55 = my birthday
np.random.seed(seed)

def decimal(a):
    """
        Tranform Z3-float into Python float
    """
    if type(a) == float:
        return a
    
    dec = simplify(a).as_decimal(10)
    if dec[-1] == "?":
        return float(dec[:-1])
    else: 
        return float(dec)

def generate_samples(num, dom, dim):
    """
        Generate the requested number of random samples in the given domain and of the given dimension
    """
    samples = (np.random.randint([dom[i][0] for i in range(dim)], [dom[i][1] + 1 for i in range(dim)], (num, dim)))
    samples = np.array([[IntVal(int(i)) for i in x] for x in samples])
    return samples

def existsTrue(l):
    """
        Check whether there exists a true element in a boolean list
    """
    for b in l:
        if b: return True
    return False

def extract_abstract_transitions(adj_matrix):
    """
        Extract abstract transition function as graph
    """
    G = nx.DiGraph()
    r = np.array([[as_bool(e) for e in r] for r in adj_matrix])

    for i in range(len(r)):
        if not existsTrue(r[i]):
            r[i][i] = True
        
    for i in range(len(r)):
        for j in np.nonzero(r[i])[0].tolist():
            G.add_edge('%s' % i, '%s' % j)
    return G


def draw_quotient(adj_matrix, exp : Experiment, save = False):
    """
        Draw network graph of obtained quotient 
    """
    fig = plt.figure()
    nx.draw_networkx(extract_abstract_transitions(adj_matrix))
    if save:
        fig.savefig('./figures/{}_quotient.png'.format(exp.name), dpi = 800, bbox_inches='tight')

def as_real(x):
    return float(x.numerator_as_long()) / float(x.denominator_as_long())

def as_bool(x):
    try:
        return bool(x)
    except:
        return 0


def extract_learner(s : Solver, model_params, adjacency_params, rank_params, partitions,verbose = False):
    """
        Extract obtained solution from the solver
    """
    sat = s.check()
    if verbose: print("Checking #Constraints:", len(s.assertions()))
    if verbose: print("Result:", sat)

    m = s.model()
    adj = [ [ m.evaluate(adjacency_params[i][j]) for j in range(len(partitions)) ] for i in range(len(partitions)) ]
    params = [m.evaluate(param) for param in model_params]
    rankp = [[m.evaluate(param) for param in l] for l in rank_params]

    if verbose:
        print("Obtained BDT Parameters:")
        for i in range(len(params)):
            if not(type(params[i]) == ArithRef):
                print(model_params[i],":", decimal(params[i]))
            else:
                print(model_params[i],":", "-") #params[i])
        
        print("Obtained Ranking Parameters:")
        for i in range(len(rankp)):
            for j in range(len(rankp[i])):
                if not(type(rankp[i][j]) == ArithRef):
                    print(rank_params[i][j],":", decimal(rankp[i][j]))
                else:
                    print(rank_params[i][j],":", "-")#rankp[i][j])
    
    return params, adj, rankp

def save_results(model_params, adjacency_params, rank_params, exp: Experiment):
    """
        Safe obtained parameters to file. 
    """
    # Re-generate names for parameters
    adjacency_param_names = [[Bool("a_%s_%s" % (i, j)) for j in range(exp.num_partitions)] for i in range(exp.num_partitions)]
    model_param_names = [Real("p_%s" % i) for i in range(exp.num_params)] + [Real("a_%s" % i) for i in range(exp.num_coefficients)]
    rank_param_names = [[Real("u_%s_%s" % (j, i)) for j in range(exp.dim)] + [Real("c_%s" % i)] for i in range(exp.num_partitions)]
    
    r = np.array([[as_bool(e) for e in r] for r in adjacency_params])
    

    for i in range(len(r)):
        if not existsTrue(r[i]):
            r[i][i] = True

    with open('./results/{}_parameters.txt'.format(exp.name),"w") as file:
        print("Obtained BDT Parameters:", file=file)
        for i in range(len(model_params)):
            if not(type(model_params[i]) == ArithRef):
                print(model_param_names[i],":", decimal(model_params[i]), file = file)
            else:
                print(model_param_names[i],":", "-", file = file)
        
        print("Obtained Ranking Parameters:",file = file)
        for i in range(len(rank_params)):
            for j in range(len(rank_param_names[i])):
                if not(type(rank_params[i][j]) == ArithRef):
                    print(rank_param_names[i][j],":", decimal(rank_params[i][j]), file = file)
                else:
                    print(rank_param_names[i][j],":", "-", file = file)
        print("Obtained Abstract Adjacency Matrix:",file = file)
        for i in range(len(adjacency_params)):
            row = ""
            for j in range(len(adjacency_params[0])):
                row += str(adjacency_param_names[i][j]) + " : " 
                row += str(bool(r[i][j])) + "  "
                
            print(row, file = file)
        
    