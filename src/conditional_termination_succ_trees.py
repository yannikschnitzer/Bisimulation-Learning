"""
 Conditional Termination Benchmarks with some benchmarks adapted from the 
 termination category of the SV-Comp [cite]. 
"""

from binary_decision_trees import *
from z3 import *

__author__ = "Yannik Schnitzer"
__copyright__ = "Copyright 2024, Yannik Schnitzer"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "yannik.schnitzer@cs.ox.ac.uk"
__status__ = "Experimental - Artifact Evaluation"


"""
    One-step transition functions for the conditional termination benchmarks.
"""

# Conditional Termination - term-loop-1
#
# while(x != 0):
#   x--;
#
# Dimension: 2
# Notes: Set valid variables in domain to bound x[1] to {0,1}
def successor_term_loop_1(x):
    y = [i for i in x]

    valid_vars = True #And(x[0] >= -r ,x[0] <= r, x[1] >= 0,x[1] <= 1)

    y[0] = simplify(If(valid_vars, If(Or(x[0] == 0, y[1] == 1), x[0], x[0] - 1), y[0]))
    y[1] = simplify(If(valid_vars, If(Or(x[0] == 0, y[1] == 1) , 1, 0), y[1])) # Variable y[1] marks whether program terminated, y[1] = 1 <-> terminated

    return y


# Conditional Termination - term-loop-2
#
# while(x > 0):
#   x = x + y;
#
# Dimension: 2
def successor_term_loop_2(x):
    y = [i for i in x]

    valid_vars = True #And(x[0] >= -r ,x[0] <= r)

    y[0] = simplify(If(valid_vars, If(x[0] <= 0, x[0], x[0] + x[1]), y[0]))

    return y

# Conditional Termination - audio-compr
#
# while(0 <= l_var < 1073741824):
#   x = x * 2;
#
# Dimension: 1
def successor_audio_compr(x):
    y = [i for i in x]

    valid_vars = True # And(x[0] >= -r ,x[0] <= r)

    y[0] = simplify(If(valid_vars, If(Or(x[0] < 0, x[0] >= 1073741824), x[0], 2 * x[0]), y[0]))

    return y

# Conditional Termination - euclid
#
# while(x != y):
#   if (x > y) {
#       x = x - y;
#   } else {
#       y = y - x;
#   }
#
# Dimension: 2
def successor_euclid(x):
    y = [i for i in x]

    valid_vars = And(Not(y[0] == y[1]))

    y[0] = simplify(If(valid_vars, If(x[0] <= x[1], x[0], x[0] - x[1]), y[0]))
    y[1] = simplify(If(valid_vars, If(x[0] <= x[1], x[1] - x[0], x[1]), y[1]))

    return y


# Conditional Termination - greater
#
# while(x >= 0):
#   if (y >= x) {
#       x--;
#   }
#
# Dimension: 2
def successor_greater(x):
    y = [i for i in x]

    valid_vars = And(x[0] >= 0)

    y[0] = simplify(If(valid_vars, If(x[0] <= x[1], x[0] - 1, x[0]), y[0]))

    return y

# Conditional Termination - smaller
#
# while(x >= 0):
#   if (y <= -x) {
#       x--
#   }
#
# Dimension: 2
def successor_smaller(x):
    y = [i for i in x]

    valid_vars = And(x[0] >= 0)
    y[0] = simplify(If(valid_vars, If(x[1] <= -x[0], x[0] - 1, x[0]), y[0]))

    return y

# Conditional Termination - conic
#
# while(x > 0):
#   if (y <= -x || x <= y) {
#       x--
#   }
#
# Dimension: 2
def successor_conic(x):
    y = [i for i in x]

    valid_vars = And(x[0] >= 0)

    y[0] = simplify(If(valid_vars, If(Or(x[1] <= -x[0], x[0] <= x[1]), x[0] - 1, x[0]), y[0]))

    return y

# Termination - disjunction
#
# while(x < y || x < z){
#   x++;
# }
#   
# Dimension: 3
def successor_disjunction(x):
    y = [i for i in x]

    valid_vars = True #And(x[0] >= -r ,x[0] <= r)

    y[0] = simplify(If(valid_vars, If(Or(x[0] < x[1], x[0] < x[2]), x[0] + 1,x[0]), y[0]))

    return y

# Conditional Termination - parallel
#
# while (x > 0 || y > 0) {
# 	if (x > 0) {
# 		x = x - 1;
# 	} else {
# 		y = y - 1;
# 	}
# }
#	return 0;
#
# Dimension: 2
def successor_parallel(x):
    y = [i for i in x]

    valid_vars = Or(x[0] > 0, x[1] > 0)
    
    y[0] = simplify(If(valid_vars, If(x[0] > 0, y[0] - 1, y[0]), y[0]))
    y[1] = simplify(If(valid_vars, If(x[0] > 0, y[1], y[1] - 1), y[1]))

    return y

# Conditional Termination - quadratic
#
# while(x <= M):
#   x = x ** 2;
#
# Dimension: 1
def successor_quadratic(x):
    M = 1000
    y = [i for i in x]

    valid_vars = And(x[0] >= 0 ,x[0] <= M)

    y[0] = simplify(If(valid_vars, x[0] * x[0], x[0]))

    return y

# Conditional Termination - cubic 
#
# while(x <= M):
#   x = 4 * x ** 3;
# 
# Dimension: 1
def successor_cubic(x):
    M = 10000
    y = [i for i in x]

    valid_vars = x[0] <= M

    y[0] = simplify(If(valid_vars, 4 *  x[0] * x[0] * x[0], x[0]))

    return y


# Conditional Termination - nlr-cond
#
# while(x ** 3 <= 100):
#   if (x) {
#       x = x ** 3;
#   }
#
# Dimension: 1
def successor_nlr_cond(x):
    y = [i for i in x]

    valid_vars = And(x[0]*x[0]+x[0] <= 100)
    y[0] = simplify(If(valid_vars, x[0] * x[0] * x[0], x[0]))

    return y


'''
    Binary Decision Tree Templates 
'''

# BDT Template - term-loop-1
# 
# Labelling Function: x[1] = 0 -> not-terminated, x[1] = 1 -> terminated
def bdt_term_loop_1(params, x, num_params, partitions):
        b = BDTNodePoly([RealVal(0),RealVal(1)],x, RealVal(0), 
                BDTNodePoly([params[num_params], params[num_params+1]], x, params[0],
                                BDTLeave(partitions[0]), BDTLeave(partitions[1])),
                BDTLeave(partitions[2])
                )
        return b.formula(), b

# BDT Template - term-loop-2
# 
# Labelling Function: x[0] > 0 -> not-terminated, x[0] <= 1 -> terminated
def bdt_term_loop_2(params, x, num_params, partitions):
        b = BDTNodePoly([RealVal(1),RealVal(0)],x, RealVal(0), 
                BDTLeave(partitions[2]),
                BDTNodePoly([params[num_params], params[num_params+1]], x, params[0],
                                BDTLeave(partitions[0]), BDTLeave(partitions[1]))
                
                )
        return b.formula(), b

# BDT Template - audio-compr
# 
# Labelling Function: x[0] > 0 -> not-terminated, x[0] <= 1 -> terminated
def bdt_audio_compr(params, x, num_params, partitions):
        b = BDTNodePoly([RealVal(1)], x, RealVal(-1), 
                BDTLeave(partitions[2]),
                BDTNodePoly([RealVal(1)] , x, RealVal(1073741823),
                        BDTNodePoly([params[num_params]], x, params[0],
                                        BDTLeave(partitions[0]), BDTLeave(partitions[1])),
                        BDTLeave(partitions[2])
                        )
                )
        return b.formula(), b

# BDT Template - euclid
# 
# Labelling Function: x[0] != x[1] -> not-terminated, x[0] = x[1] -> terminated
def bdt_euclid(params, x, num_params, partitions):
        b = BDTNodePoly([RealVal(1),RealVal(-1)],x, RealVal(0), 
                BDTNodePoly([RealVal(-1),RealVal(1)],x, RealVal(0), 
                        BDTLeave(partitions[2]),
                        BDTNodePoly([params[num_params], params[num_params+1]], x, params[0],
                                        BDTLeave(partitions[0]), BDTLeave(partitions[1]))
                ),
                BDTNodePoly([params[num_params+2], params[num_params+3]], x, params[1],
                                        BDTLeave(partitions[0]), BDTLeave(partitions[1]))
        )
        return b.formula(), b


# BDT Template - greater
# 
# Labelling Function: x[0] >= 0 -> not-terminated, x[0] < 0 -> terminated
def bdt_greater(params, x, num_params, partitions):
        b = BDTNodePoly([RealVal(-1),RealVal(0)],x, RealVal(0), 
                BDTNodePoly([params[num_params], params[num_params+1]], x, params[0],
                                BDTLeave(partitions[0]), BDTLeave(partitions[1])),
                BDTLeave(partitions[2])
                )
        return b.formula(), b

# BDT Template - smaller
# 
# Labelling Function: x[0] >= 0 -> not-terminated, x[0] < 0 -> terminated
def bdt_smaller(params, x, num_params, partitions):
        b = BDTNodePoly([RealVal(-1),RealVal(0)],x, RealVal(0), 
                BDTNodePoly([params[num_params], params[num_params+1]], x, params[0],
                                BDTLeave(partitions[0]), BDTLeave(partitions[1])),
                BDTLeave(partitions[2])
                )
        return b.formula(), b

# BDT Template - conic
# 
# Labelling Function: x[0] >= 0 -> not-terminated, x[0] < 0 -> terminated
def bdt_conic(params, x, num_params, partitions):
        b = BDTNodePoly([RealVal(-1),RealVal(0)],x, RealVal(0), 
                BDTNodePoly([params[num_params], params[num_params+1]], x, params[0],
                                BDTLeave(partitions[0]), 
                                BDTNodePoly([params[num_params+2], params[num_params+3]], x, params[1],
                                            BDTLeave(partitions[0]), 
                                            BDTLeave(partitions[1])
                                )
                        ),
                BDTLeave(partitions[2])
                )
        return b.formula(), b

# BDT Template - disjunction
# 
# Labelling Function: x[0] < x[1] or x[0] < x[2] -> not-terminated, x[0] >= x[1] and x[0] >= x[2]  -> terminated
def bdt_disjunction(params, x, num_params, partitions):
        b = BDTNodePoly([RealVal(-1),RealVal(1),RealVal(0)],x, RealVal(0), 
                BDTLeave(partitions[2]),
                BDTNodePoly([RealVal(-1),RealVal(0),RealVal(1)],x, RealVal(0), 
                        BDTLeave(partitions[2]),
                        BDTNodePoly([params[num_params], params[num_params+1], params[num_params + 2]], x, params[0],
                                        BDTLeave(partitions[0]), BDTLeave(partitions[1]))
                        
                        )
        )
        return b.formula(), b


# BDT Template - parallel
# 
# Labelling Function: x[0] > 0 or x[1] > 0 -> not-terminated, x[0] <= 0 and x[1] <= 0  -> terminated
def bdt_parallel(params, x, num_params, partitions):
        b = BDTNodePoly([RealVal(1),RealVal(0)],x, RealVal(0), 
                BDTNodePoly([RealVal(0),RealVal(1)],x, RealVal(0), 
                        BDTLeave(partitions[2]),
                        BDTNodePoly([params[num_params], params[num_params+1]], x, params[0],
                                        BDTLeave(partitions[0]), BDTLeave(partitions[1]))
                ),
                BDTNodePoly([params[num_params+2], params[num_params+3]], x, params[1],
                                        BDTLeave(partitions[0]), BDTLeave(partitions[1]))
        )
        return b.formula(), b

# BDT Template - quadratic
# 
# Labelling Function: x[0] < M -> not-terminated, x[0] >= M -> terminated
def bdt_quadratic(params, x, num_params, partitions):
        b = BDTNodePoly([RealVal(1)],x, RealVal(1000), 
                BDTNodePoly([params[num_params]],x, params[0], 
                        BDTLeave(partitions[0]),
                        BDTNodePoly([params[num_params + 1]], x, params[1],
                                        BDTLeave(partitions[1]), BDTLeave(partitions[2]))
                ),
                BDTLeave(partitions[3])
        )
        return b.formula(), b

# BDT Template - cubic
# 
# Labelling Function: x[0] < M -> not-terminated, x[0] >= M -> terminated
def bdt_cubic(params, x, num_params, partitions):
        b = BDTNodePoly([RealVal(1)],x, RealVal(10000), 
                BDTNodePoly([params[num_params]],x, params[0], 
                        BDTLeave(partitions[0]),
                        BDTNodePoly([params[num_params + 1]], x, params[1],
                                        BDTLeave(partitions[1]), BDTLeave(partitions[2]))
                ),
                BDTLeave(partitions[3])
        )
        return b.formula(), b

# BDT Template - nlr-cond
# 
# Labelling Function: x[0] ** 3 * < M -> not-terminated, x[0] ** 3 >= M -> terminated
def bdt_nlr_cond(params, x, num_params, partitions):
        b = BDTNode(x[0]*x[0]*x[0], RealVal(100), 
                BDTNodePoly([params[num_params]],x, params[0], 
                        BDTLeave(partitions[0]),
                        BDTNodePoly([params[num_params + 1]], x, params[1],
                                        BDTLeave(partitions[1]), BDTLeave(partitions[2]))
                ),
                BDTLeave(partitions[3])
        )
        return b.formula(), b
