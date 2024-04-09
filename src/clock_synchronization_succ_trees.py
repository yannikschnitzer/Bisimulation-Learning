"""
 Clock Synchronization Benchmarks.
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
    One-step transition functions for the clock synchronization benchmarks.
"""

# TTEthernet Safe 10
def successor_tte_sf_10(x): 
    r = 10 # Dicsretizazion Parameter
    y = [i for i in x]
    valid_clocks = And(x[1] - x[0] <= r, x[0] <= r, x[1] <= 2.5 * r)

    y[0] = simplify(If(valid_clocks, If(x[0] == r, 0, y[0] + 1), y[0]))
    y[1] = simplify(If(valid_clocks, If(x[0] == r, 0, y[1] + 2), y[1]))
    return y

# TTEthernet Safe 100
def successor_tte_sf_100(x): 
    r = 100 # Dicsretizazion Parameter
    y = [i for i in x]
    valid_clocks = And(x[1] - x[0] <= r, x[0] <= r, x[1] <= 2.5 * r)

    y[0] = simplify(If(valid_clocks, If(x[0] == r, 0, y[0] + 1), y[0]))
    y[1] = simplify(If(valid_clocks, If(x[0] == r, 0, y[1] + 2), y[1]))
    return y

# TTEthernet Safe 1000
def successor_tte_sf_1000(x): 
    r = 1000 # Dicsretizazion Parameter
    y = [i for i in x]
    valid_clocks = And(x[1] - x[0] <= r, x[0] <= r, x[1] <= 2.5 * r)

    y[0] = simplify(If(valid_clocks, If(x[0] == r, 0, y[0] + 1), y[0]))
    y[1] = simplify(If(valid_clocks, If(x[0] == r, 0, y[1] + 2), y[1]))
    return y

# TTEthernet Safe 2000
def successor_tte_sf_2000(x): 
    r = 2000 # Dicsretizazion Parameter
    y = [i for i in x]
    valid_clocks = And(x[1] - x[0] <= r, x[0] <= r, x[1] <= 2.5 * r)

    y[0] = simplify(If(valid_clocks, If(x[0] == r, 0, y[0] + 1), y[0]))
    y[1] = simplify(If(valid_clocks, If(x[0] == r, 0, y[1] + 2), y[1]))
    return y


# TTEthernet Safe 5000
def successor_tte_sf_5000(x): 
    r = 5000 # Dicsretizazion Parameter
    y = [i for i in x]
    valid_clocks = And(x[1] - x[0] <= r, x[0] <= r, x[1] <= 2.5 * r)

    y[0] = simplify(If(valid_clocks, If(x[0] == r, 0, y[0] + 1), y[0]))
    y[1] = simplify(If(valid_clocks, If(x[0] == r, 0, y[1] + 2), y[1]))
    return y


# TTEthernet Safe 10000
def successor_tte_sf_10000(x): 
    r = 10000 # Dicsretizazion Parameter
    y = [i for i in x]
    valid_clocks = And(x[1] - x[0] <= r, x[0] <= r, x[1] <= 2.5 * r)

    y[0] = simplify(If(valid_clocks, If(x[0] == r, 0, y[0] + 1), y[0]))
    y[1] = simplify(If(valid_clocks, If(x[0] == r, 0, y[1] + 2), y[1]))
    return y


# TTEthernet Unsafe 10
def successor_tte_usf_10(x): 
    r = 10 #Dicsretizazion Parameter
    y = [i for i in x]
    valid_clocks = And(x[1] - x[0] <= r, x[0] <= r, x[1] <= 2.5*r)

    y[0] = simplify(If(valid_clocks, y[0] + 1, y[0]))
    y[1] = simplify(If(valid_clocks, y[1] + 2, y[1]))
    return y

# TTEthernet Unsafe 100
def successor_tte_usf_100(x): 
    r = 100 #Dicsretizazion Parameter
    y = [i for i in x]
    valid_clocks = And(x[1] - x[0] <= r, x[0] <= r, x[1] <= 2.5*r)

    y[0] = simplify(If(valid_clocks, y[0] + 1, y[0]))
    y[1] = simplify(If(valid_clocks, y[1] + 2, y[1]))
    return y


# TTEthernet Unsafe 1000
def successor_tte_usf_1000(x): 
    r = 1000 #Dicsretizazion Parameter
    y = [i for i in x]
    valid_clocks = And(x[1] - x[0] <= r, x[0] <= r, x[1] <= 2.5*r)

    y[0] = simplify(If(valid_clocks, y[0] + 1, y[0]))
    y[1] = simplify(If(valid_clocks, y[1] + 2, y[1]))
    return y

# TTEthernet Unsafe 2000
def successor_tte_usf_2000(x): 
    r = 2000 #Dicsretizazion Parameter
    y = [i for i in x]
    valid_clocks = And(x[1] - x[0] <= r, x[0] <= r, x[1] <= 2.5*r)

    y[0] = simplify(If(valid_clocks, y[0] + 1, y[0]))
    y[1] = simplify(If(valid_clocks, y[1] + 2, y[1]))
    return y

# TTEthernet Unsafe 5000
def successor_tte_usf_5000(x): 
    r = 5000 #Dicsretizazion Parameter
    y = [i for i in x]
    valid_clocks = And(x[1] - x[0] <= r, x[0] <= r, x[1] <= 2.5*r)

    y[0] = simplify(If(valid_clocks, y[0] + 1, y[0]))
    y[1] = simplify(If(valid_clocks, y[1] + 2, y[1]))
    return y

# TTEthernet Unsafe 10000
def successor_tte_usf_10000(x): 
    r = 10000 #Dicsretizazion Parameter
    y = [i for i in x]
    valid_clocks = And(x[1] - x[0] <= r, x[0] <= r, x[1] <= 2.5*r)

    y[0] = simplify(If(valid_clocks, y[0] + 1, y[0]))
    y[1] = simplify(If(valid_clocks, y[1] + 2, y[1]))
    return y

# Interactive Convergence Safe 10
def successor_con_sf_10(x):
    r = 10
    y = [i for i in x]

    valid_clocks = And(x[0] <= r, x[1] - x[0] <= r,x[1] <= 2.5*r)
    in_range = x[0] - x[1] <= r
    reset =  x[0] == r


    y[0] = simplify(If(valid_clocks, If(reset, If(in_range, 0, y[0] + 1), y[0] + 1), y[0]))
    y[1] = simplify(If(valid_clocks, If(reset, If(in_range, 0, y[1] + 2), y[1] + 2), y[1]))

    return y

# Interactive Convergence Safe 100
def successor_con_sf_100(x):
    r = 100
    y = [i for i in x]

    valid_clocks = And(x[0] <= r, x[1] - x[0] <= r,x[1] <= 2.5*r)
    in_range = x[0] - x[1] <= r
    reset =  x[0] == r


    y[0] = simplify(If(valid_clocks, If(reset, If(in_range, 0, y[0] + 1), y[0] + 1), y[0]))
    y[1] = simplify(If(valid_clocks, If(reset, If(in_range, 0, y[1] + 2), y[1] + 2), y[1]))

    return y

# Interactive Convergence Safe 1000
def successor_con_sf_1000(x):
    r = 1000
    y = [i for i in x]

    valid_clocks = And(x[0] <= r, x[1] - x[0] <= r,x[1] <= 2.5*r)
    in_range = x[0] - x[1] <= r
    reset =  x[0] == r


    y[0] = simplify(If(valid_clocks, If(reset, If(in_range, 0, y[0] + 1), y[0] + 1), y[0]))
    y[1] = simplify(If(valid_clocks, If(reset, If(in_range, 0, y[1] + 2), y[1] + 2), y[1]))

    return y

# Interactive Convergence Safe 2000
def successor_con_sf_2000(x):
    r = 2000
    y = [i for i in x]

    valid_clocks = And(x[0] <= r, x[1] - x[0] <= r,x[1] <= 2.5*r)
    in_range = x[0] - x[1] <= r
    reset =  x[0] == r


    y[0] = simplify(If(valid_clocks, If(reset, If(in_range, 0, y[0] + 1), y[0] + 1), y[0]))
    y[1] = simplify(If(valid_clocks, If(reset, If(in_range, 0, y[1] + 2), y[1] + 2), y[1]))

    return y

# Interactive Convergence Safe 5000
def successor_con_sf_5000(x):
    r = 5000
    y = [i for i in x]

    valid_clocks = And(x[0] <= r, x[1] - x[0] <= r,x[1] <= 2.5*r)
    in_range = x[0] - x[1] <= r
    reset =  x[0] == r


    y[0] = simplify(If(valid_clocks, If(reset, If(in_range, 0, y[0] + 1), y[0] + 1), y[0]))
    y[1] = simplify(If(valid_clocks, If(reset, If(in_range, 0, y[1] + 2), y[1] + 2), y[1]))

    return y

# Interactive Convergence Safe 10000
def successor_con_sf_10000(x):
    r = 10000
    y = [i for i in x]

    valid_clocks = And(x[0] <= r, x[1] - x[0] <= r,x[1] <= 2.5*r)
    in_range = x[0] - x[1] <= r
    reset =  x[0] == r


    y[0] = simplify(If(valid_clocks, If(reset, If(in_range, 0, y[0] + 1), y[0] + 1), y[0]))
    y[1] = simplify(If(valid_clocks, If(reset, If(in_range, 0, y[1] + 2), y[1] + 2), y[1]))

    return y


# Interactive Convergence Unsafe 10
def successor_con_usf_10(x):
    r = 10
    y = [i for i in x]

    valid_clocks = And(x[1] - x[0] <= r, x[0] <= r, x[1] <= 2.5*r)

    y[0] = simplify(If(valid_clocks, y[0] + 1, y[0]))
    y[1] = simplify(If(valid_clocks, y[1] + 2, y[1]))

    return y

# Interactive Convergence Unsafe 100
def successor_con_usf_100(x):
    r = 100
    y = [i for i in x]

    valid_clocks = And(x[1] - x[0] <= r, x[0] <= r, x[1] <= 2.5*r)

    y[0] = simplify(If(valid_clocks, y[0] + 1, y[0]))
    y[1] = simplify(If(valid_clocks, y[1] + 2, y[1]))

    return y

# Interactive Convergence Unsafe 1000
def successor_con_usf_1000(x):
    r = 1000
    y = [i for i in x]

    valid_clocks = And(x[1] - x[0] <= r, x[0] <= r, x[1] <= 2.5*r)

    y[0] = simplify(If(valid_clocks, y[0] + 1, y[0]))
    y[1] = simplify(If(valid_clocks, y[1] + 2, y[1]))

    return y

# Interactive Convergence Unsafe 2000
def successor_con_usf_2000(x):
    r = 2000
    y = [i for i in x]

    valid_clocks = And(x[1] - x[0] <= r, x[0] <= r, x[1] <= 2.5*r)

    y[0] = simplify(If(valid_clocks, y[0] + 1, y[0]))
    y[1] = simplify(If(valid_clocks, y[1] + 2, y[1]))

    return y

# Interactive Convergence Unsafe 5000
def successor_con_usf_5000(x):
    r = 5000
    y = [i for i in x]

    valid_clocks = And(x[1] - x[0] <= r, x[0] <= r, x[1] <= 2.5*r)

    y[0] = simplify(If(valid_clocks, y[0] + 1, y[0]))
    y[1] = simplify(If(valid_clocks, y[1] + 2, y[1]))

    return y

# Interactive Convergence Unsafe 10000
def successor_con_usf_10000(x):
    r = 10000
    y = [i for i in x]

    valid_clocks = And(x[1] - x[0] <= r, x[0] <= r, x[1] <= 2.5*r)

    y[0] = simplify(If(valid_clocks, y[0] + 1, y[0]))
    y[1] = simplify(If(valid_clocks, y[1] + 2, y[1]))

    return y

# BDT Template - 
#
# 
# Labelling Function: x[1] -  x[0] <= r -> safe, x[1] - x[0] > r -> violated
def bdt_tte_10(params, x, num_params, partitions):
        r = 10 # Discretization Parameter
        b = BDTNodePoly([RealVal(-1),RealVal(1)],x, RealVal(r), 
                BDTNodePoly([params[num_params], params[num_params+1]], x, params[0],
                                BDTLeave(partitions[0]), BDTLeave(partitions[1])),
                BDTLeave(partitions[2])
                )
        return b.formula(), b

# BDT Template - 
#
# 
# Labelling Function: x[1] -  x[0] <= r -> safe, x[1] - x[0] > r -> violated
def bdt_tte_100(params, x, num_params, partitions):
        r = 100 # Discretization Parameter
        b = BDTNodePoly([RealVal(-1),RealVal(1)],x, RealVal(r), 
                BDTNodePoly([params[num_params], params[num_params+1]], x, params[0],
                                BDTLeave(partitions[0]), BDTLeave(partitions[1])),
                BDTLeave(partitions[2])
                )
        return b.formula(), b

# BDT Template - 
#
# 
# Labelling Function: x[1] -  x[0] <= r -> safe, x[1] - x[0] > r -> violated
def bdt_tte_1000(params, x, num_params, partitions):
        r = 1000 # Discretization Parameter
        b = BDTNodePoly([RealVal(-1),RealVal(1)],x, RealVal(r), 
                BDTNodePoly([params[num_params], params[num_params+1]], x, params[0],
                                BDTLeave(partitions[0]), BDTLeave(partitions[1])),
                BDTLeave(partitions[2])
                )
        return b.formula(), b

# BDT Template - 
#
# 
# Labelling Function: x[1] -  x[0] <= r -> safe, x[1] - x[0] > r -> violated
def bdt_tte_2000(params, x, num_params, partitions):
        r = 2000 # Discretization Parameter
        b = BDTNodePoly([RealVal(-1),RealVal(1)],x, RealVal(r), 
                BDTNodePoly([params[num_params], params[num_params+1]], x, params[0],
                                BDTLeave(partitions[0]), BDTLeave(partitions[1])),
                BDTLeave(partitions[2])
                )
        return b.formula(), b


# BDT Template - 
#
# 
# Labelling Function: x[1] -  x[0] <= r -> safe, x[1] - x[0] > r -> violated
def bdt_tte_5000(params, x, num_params, partitions):
        r = 5000 # Discretization Parameter
        b = BDTNodePoly([RealVal(-1),RealVal(1)],x, RealVal(r), 
                BDTNodePoly([params[num_params], params[num_params+1]], x, params[0],
                                BDTLeave(partitions[0]), BDTLeave(partitions[1])),
                BDTLeave(partitions[2])
                )
        return b.formula(), b


# BDT Template - 
#
# 
# Labelling Function: x[1] -  x[0] <= r -> safe, x[1] - x[0] > r -> violated
def bdt_tte_10000(params, x, num_params, partitions):
        r = 10000 # Discretization Parameter
        b = BDTNodePoly([RealVal(-1),RealVal(1)],x, RealVal(r), 
                BDTNodePoly([params[num_params], params[num_params+1]], x, params[0],
                                BDTLeave(partitions[0]), BDTLeave(partitions[1])),
                BDTLeave(partitions[2])
                )
        return b.formula(), b

# BDT Template - 
#
# 
# Labelling Function: x[1] -  x[0] <= r -> safe, x[1] - x[0] > r -> violated
def bdt_con_10(params, x, num_params, partitions):
        r = 10 # Discretization Parameter
        b = BDTNodePoly([RealVal(-1),RealVal(1)],x, RealVal(r), 
                BDTNodePoly([params[num_params], params[num_params+1]], x, params[0],
                                BDTLeave(partitions[0]), BDTLeave(partitions[1])),
                BDTLeave(partitions[2])
                )
        return b.formula(), b

# BDT Template - 
#
# 
# Labelling Function: x[1] -  x[0] <= r -> safe, x[1] - x[0] > r -> violated
def bdt_con_100(params, x, num_params, partitions):
        r = 100 # Discretization Parameter
        b = BDTNodePoly([RealVal(-1),RealVal(1)],x, RealVal(r), 
                BDTNodePoly([params[num_params], params[num_params+1]], x, params[0],
                                BDTLeave(partitions[0]), BDTLeave(partitions[1])),
                BDTLeave(partitions[2])
                )
        return b.formula(), b

# BDT Template - 
#
# 
# Labelling Function: x[1] -  x[0] <= r -> safe, x[1] - x[0] > r -> violated
def bdt_con_1000(params, x, num_params, partitions):
        r = 1000 # Discretization Parameter
        b = BDTNodePoly([RealVal(-1),RealVal(1)],x, RealVal(r), 
                BDTNodePoly([params[num_params], params[num_params+1]], x, params[0],
                                BDTLeave(partitions[0]), BDTLeave(partitions[1])),
                BDTLeave(partitions[2])
                )
        return b.formula(), b

# BDT Template - 
#
# 
# Labelling Function: x[1] -  x[0] <= r -> safe, x[1] - x[0] > r -> violated
def bdt_con_2000(params, x, num_params, partitions):
        r = 2000 # Discretization Parameter
        b = BDTNodePoly([RealVal(-1),RealVal(1)],x, RealVal(r), 
                BDTNodePoly([params[num_params], params[num_params+1]], x, params[0],
                                BDTLeave(partitions[0]), BDTLeave(partitions[1])),
                BDTLeave(partitions[2])
                )
        return b.formula(), b


# BDT Template - 
#
# 
# Labelling Function: x[1] -  x[0] <= r -> safe, x[1] - x[0] > r -> violated
def bdt_con_5000(params, x, num_params, partitions):
        r = 5000 # Discretization Parameter
        b = BDTNodePoly([RealVal(-1),RealVal(1)],x, RealVal(r), 
                BDTNodePoly([params[num_params], params[num_params+1]], x, params[0],
                                BDTLeave(partitions[0]), BDTLeave(partitions[1])),
                BDTLeave(partitions[2])
                )
        return b.formula(), b


# BDT Template - 
#
# 
# Labelling Function: x[1] -  x[0] <= r -> safe, x[1] - x[0] > r -> violated
def bdt_con_10000(params, x, num_params, partitions):
        r = 10000 # Discretization Parameter
        b = BDTNodePoly([RealVal(-1),RealVal(1)],x, RealVal(r), 
                BDTNodePoly([params[num_params], params[num_params+1]], x, params[0],
                                BDTLeave(partitions[0]), BDTLeave(partitions[1])),
                BDTLeave(partitions[2])
                )
        return b.formula(), b



