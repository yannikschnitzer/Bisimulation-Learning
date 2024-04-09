"""
 Classes for using Binary Decision Tree (BDT) templates with arbitary or linear predicates.
"""

from utils import *
from z3 import *
import numpy as np


__author__ = "Yannik Schnitzer"
__copyright__ = "Copyright 2024, Yannik Schnitzer"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "yannik.schnitzer@cs.ox.ac.uk"
__status__ = "Experimental - Artifact Evaluation"


'''
   BDT Leave representing an outcome, i.e., classificaiton.  
'''
class BDTLeave:
    def __init__(self, outcome):
        self.outcome = outcome

    def formula(self):
        return self.outcome

    def robust_formula(self):
        return self.outcome
    
    def pred(self, x, robust=False):
        return self.outcome.as_long()
    
'''
   General BDT Node with arbitary predicate formula. Splits into left and right subtree. 
'''
class BDTNode:
    def __init__(self, condition, param, res_l, res_r):
        self.condition = condition
        self.param = param
        self.res_l = res_l
        self.res_r = res_r

    def formula(self):
        return If(self.condition <= self.param, self.res_l.formula(), self.res_r.formula())

'''
   Linear BDT Node. Takes a list of coefficients \vec{a}, variables \vec{v} and a parmeter formula p, 
   and represents condition p(v) <-> \vec{a} x \vec{v} <= p. Splits into left and right subtree.
'''
class BDTNodePoly:
    def __init__(self, coefficients: list, variables: list, param, res_l, res_r):
        self.coeffs = coefficients
        self.vars = variables
        self.param = param
        self.res_l = res_l
        self.res_r = res_r

        self.condition = np.dot(coefficients, variables)

    def formula(self):
        return If(self.condition <= self.param, self.res_l.formula(), self.res_r.formula())
    

    # Prediction is only used for means visualization, to get classificaiton as long and not Z3 types.
    def pred(self, x):
        if decimal(np.dot(self.coeffs, x)) <= decimal(self.param):
            return self.res_l.pred(x)
        else:
            return self.res_r.pred(x)