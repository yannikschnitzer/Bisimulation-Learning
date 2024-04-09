"""
 Defines and runs Clock Synchronization experiments.
"""

from utils import *
from experiment import Experiment
from experiment_runner import *
from clock_synchronization_succ_trees import *
from cegis_solver import *
from visualization import *
import numpy as np

__author__ = "Yannik Schnitzer"
__copyright__ = "Copyright 2024, Yannik Schnitzer"
__license__ = "MIT"
__version__ = "1.0.0" 
__email__ = "yannik.schnitzer@cs.ox.ac.uk"
__status__ = "Experimental - Artifact Evaluation"

def run_clock_synch_experiments():
    run_experiment(exp_tte_sf_10(), benchmark_time = True, save_res = True)
    run_experiment(exp_tte_sf_100(), benchmark_time = True, save_res = True)
    run_experiment(exp_tte_sf_1000(), benchmark_time = True, save_res = True)
    run_experiment(exp_tte_sf_2000(), benchmark_time = True, save_res = True)
    run_experiment(exp_tte_sf_5000(), benchmark_time = True, save_res = True)
    run_experiment(exp_tte_sf_10000(), benchmark_time = True, save_res = True)

    run_experiment(exp_tte_usf_10(), benchmark_time = True, save_res = True)
    run_experiment(exp_tte_usf_100(), benchmark_time = True, save_res = True)
    run_experiment(exp_tte_usf_1000(), benchmark_time = True, save_res = True)
    run_experiment(exp_tte_usf_2000(), benchmark_time = True, save_res = True)
    run_experiment(exp_tte_usf_5000(), benchmark_time = True, save_res = True)
    run_experiment(exp_tte_usf_10000(), benchmark_time = True, save_res = True)

    run_experiment(exp_con_sf_10(), benchmark_time = True, save_res = True)
    run_experiment(exp_con_sf_100(), benchmark_time = True, save_res = True)
    run_experiment(exp_con_sf_1000(), benchmark_time = True, save_res = True)
    run_experiment(exp_con_sf_2000(), benchmark_time = True, save_res = True)
    run_experiment(exp_con_sf_5000(), benchmark_time = True, save_res = True)
    run_experiment(exp_con_sf_10000(), benchmark_time = True, save_res = True)

    run_experiment(exp_con_usf_10(), benchmark_time = True, save_res = True)
    run_experiment(exp_con_usf_100(), benchmark_time = True, save_res = True)
    run_experiment(exp_con_usf_1000(), benchmark_time = True, save_res = True)
    run_experiment(exp_con_usf_2000(), benchmark_time = True, save_res = True)
    run_experiment(exp_con_usf_5000(), benchmark_time = True, save_res = True)
    run_experiment(exp_con_usf_10000(), benchmark_time = True, save_res = True)


def exp_tte_sf_10():
    def domain(x):
        """
            Domain bounding variable values to reachable statespace (only for which values are considered in the conditions, the variables still run over unbounded integers)
        """
        dom = [[0, 10],
               [0, 25]]
        return And(*[simplify(And(x[i] >= dom[i][0], x[i] <= dom[i][1])) for i in range(len(dom))])

    exp = Experiment("tte-sf-10",
                      bdt_tte_10,
                      successor_tte_sf_10,
                      domain,
                      num_params = 1,
                      num_coefficients = 2,
                      num_partitions = 3,
                      dim = 2,
                      num_initial = 1
                      )
    return exp


def exp_tte_sf_100():
    def domain(x):
        """
            Domain bounding variable values to reachable statespace (only for which values are considered in the conditions, the variables still run over unbounded integers)
        """
        dom = [[0, 100],
               [0, 250]]
        return And(*[simplify(And(x[i] >= dom[i][0], x[i] <= dom[i][1])) for i in range(len(dom))])

    exp = Experiment("tte-sf-100",
                      bdt_tte_100,
                      successor_tte_sf_100,
                      domain,
                      num_params = 1,
                      num_coefficients = 2,
                      num_partitions = 3,
                      dim = 2,
                      num_initial = 5
                      )
    return exp


def exp_tte_sf_1000():
    def domain(x):
        """
            Domain bounding variable values to reachable statespace (only for which values are considered in the conditions, the variables still run over unbounded integers)
        """
        dom = [[0, 1000],
               [0, 2500]]
        return And(*[simplify(And(x[i] >= dom[i][0], x[i] <= dom[i][1])) for i in range(len(dom))])

    exp = Experiment("tte-sf-1000",
                      bdt_tte_1000,
                      successor_tte_sf_1000,
                      domain,
                      num_params = 1,
                      num_coefficients = 2,
                      num_partitions = 3,
                      dim = 2,
                      num_initial = 8
                      )
    return exp

def exp_tte_sf_2000():
    def domain(x):
        """
            Domain bounding variable v alues to reachable statespace (only for which values are considered in the conditions, the variables still run over unbounded integers)
        """
        dom = [[0, 2000],
               [0, 5000]]
        return And(*[simplify(And(x[i] >= dom[i][0], x[i] <= dom[i][1])) for i in range(len(dom))])

    exp = Experiment("tte-sf-2000",
                      bdt_tte_2000,
                      successor_tte_sf_2000,
                      domain,
                      num_params = 1,
                      num_coefficients = 2,
                      num_partitions = 3,
                      dim = 2,
                      num_initial = 8
                      )
    return exp

def exp_tte_sf_5000():
    def domain(x):
        """
            Domain bounding variable values to reachable statespace (only for which values are considered in the conditions, the variables still run over unbounded integers)
        """
        dom = [[0, 5000],
               [0, 12500]]
        return And(*[simplify(And(x[i] >= dom[i][0], x[i] <= dom[i][1])) for i in range(len(dom))])

    exp = Experiment("tte-sf-5000",
                      bdt_tte_5000,
                      successor_tte_sf_5000,
                      domain,
                      num_params = 1,
                      num_coefficients = 2,
                      num_partitions = 3,
                      dim = 2,
                      num_initial = 10
                      )
    return exp

def exp_tte_sf_10000():
    def domain(x):
        """
            Domain bounding variable values to reachable statespace (only for which values are considered in the conditions, the variables still run over unbounded integers)
        """
        dom = [[0, 10000],
               [0, 25000]]
        return And(*[simplify(And(x[i] >= dom[i][0], x[i] <= dom[i][1])) for i in range(len(dom))])

    exp = Experiment("tte-sf-10000",
                      bdt_tte_10000,
                      successor_tte_sf_10000,
                      domain,
                      num_params = 1,
                      num_coefficients = 2,
                      num_partitions = 3,
                      dim = 2,
                      num_initial = 8
                      )
    return exp

def exp_tte_usf_10():
    def domain(x):
        """
            Domain bounding variable values to reachable statespace (only for which values are considered in the conditions, the variables still run over unbounded integers)
        """
        dom = [[0, 10],
               [0, 25]]
        return And(*[simplify(And(x[i] >= dom[i][0], x[i] <= dom[i][1])) for i in range(len(dom))])

    exp = Experiment("tte-usf-10",
                      bdt_tte_10,
                      successor_tte_usf_10,
                      domain,
                      num_params = 1,
                      num_coefficients = 2,
                      num_partitions = 3,
                      dim = 2,
                      num_initial = 5
                      )
    return exp

def exp_tte_usf_100():
    def domain(x):
        """
            Domain bounding variable values to reachable statespace (only for which values are considered in the conditions, the variables still run over unbounded integers)
        """
        dom = [[0, 100],
               [0, 250]]
        return And(*[simplify(And(x[i] >= dom[i][0], x[i] <= dom[i][1])) for i in range(len(dom))])

    exp = Experiment("tte-usf-100",
                      bdt_tte_100,
                      successor_tte_usf_100,
                      domain,
                      num_params = 1,
                      num_coefficients = 2,
                      num_partitions = 3,
                      dim = 2,
                      num_initial = 10
                      )
    return exp

def exp_tte_usf_1000():
    def domain(x):
        """
            Domain bounding variable values to reachable statespace (only for which values are considered in the conditions, the variables still run over unbounded integers)
        """
        dom = [[0, 1000],
               [0, 2500]]
        return And(*[simplify(And(x[i] >= dom[i][0], x[i] <= dom[i][1])) for i in range(len(dom))])

    exp = Experiment("tte-usf-1000",
                      bdt_tte_100,
                      successor_tte_usf_1000,
                      domain,
                      num_params = 1,
                      num_coefficients = 2,
                      num_partitions = 3,
                      dim = 2,
                      num_initial = 10
                      )
    return exp

def exp_tte_usf_2000():
    def domain(x):
        """
            Domain bounding variable values to reachable statespace (only for which values are considered in the conditions, the variables still run over unbounded integers)
        """
        dom = [[0, 2000],
               [0, 5000]]
        return And(*[simplify(And(x[i] >= dom[i][0], x[i] <= dom[i][1])) for i in range(len(dom))])

    exp = Experiment("tte-usf-2000",
                      bdt_tte_2000,
                      successor_tte_usf_2000,
                      domain,
                      num_params = 1,
                      num_coefficients = 2,
                      num_partitions = 3,
                      dim = 2,
                      num_initial = 20
                      )
    return exp

def exp_tte_usf_5000():
    def domain(x):
        """
            Domain bounding variable values to reachable statespace (only for which values are considered in the conditions, the variables still run over unbounded integers)
        """
        dom = [[0, 5000],
               [0, 12500]]
        return And(*[simplify(And(x[i] >= dom[i][0], x[i] <= dom[i][1])) for i in range(len(dom))])

    exp = Experiment("tte-usf-5000",
                      bdt_tte_5000,
                      successor_tte_usf_5000,
                      domain,
                      num_params = 1,
                      num_coefficients = 2,
                      num_partitions = 3,
                      dim = 2,
                      num_initial = 20
                      )
    return exp

def exp_tte_usf_10000():
    def domain(x):
        """
            Domain bounding variable values to reachable statespace (only for which values are considered in the conditions, the variables still run over unbounded integers)
        """
        dom = [[0, 10000],
               [0, 25000]]
        return And(*[simplify(And(x[i] >= dom[i][0], x[i] <= dom[i][1])) for i in range(len(dom))])

    exp = Experiment("tte-usf-10000",
                      bdt_tte_10000,
                      successor_tte_usf_10000,
                      domain,
                      num_params = 1,
                      num_coefficients = 2,
                      num_partitions = 3,
                      dim = 2,
                      num_initial = 30
                      )
    return exp

def exp_con_sf_10():
    def domain(x):
        """
            Domain bounding variable values to reachable statespace (only for which values are considered in the conditions, the variables still run over unbounded integers)
        """
        dom = [[0, 10],
               [0, 20]]
        return And(*[simplify(And(x[i] >= dom[i][0], x[i] <= dom[i][1])) for i in range(len(dom))])

    exp = Experiment("con-sf-10",
                      bdt_con_10,
                      successor_con_sf_10,
                      domain,
                      num_params = 1,
                      num_coefficients = 2,
                      num_partitions = 3,
                      dim = 2,
                      num_initial = 2
                      )
    return exp

def exp_con_sf_100():
    def domain(x):
        """
            Domain bounding variable values to reachable statespace (only for which values are considered in the conditions, the variables still run over unbounded integers)
        """
        dom = [[0, 100],
               [0, 250]]
        return And(*[simplify(And(x[i] >= dom[i][0], x[i] <= dom[i][1])) for i in range(len(dom))])

    exp = Experiment("con-sf-100",
                      bdt_con_100,
                      successor_con_sf_100,
                      domain,
                      num_params = 1,
                      num_coefficients = 2,
                      num_partitions = 3,
                      dim = 2,
                      num_initial = 2
                      )
    return exp

def exp_con_sf_1000():
    def domain(x):
        """
            Domain bounding variable values to reachable statespace (only for which values are considered in the conditions, the variables still run over unbounded integers)
        """
        dom = [[0, 1000],
               [0, 2500]]
        return And(*[simplify(And(x[i] >= dom[i][0], x[i] <= dom[i][1])) for i in range(len(dom))])

    exp = Experiment("con-sf-1000",
                      bdt_con_1000,
                      successor_con_sf_1000,
                      domain,
                      num_params = 1,
                      num_coefficients = 2,
                      num_partitions = 3,
                      dim = 2,
                      num_initial = 5
                      )
    return exp

def exp_con_sf_2000():
    def domain(x):
        """
            Domain bounding variable values to reachable statespace (only for which values are considered in the conditions, the variables still run over unbounded integers)
        """
        dom = [[0, 2000],
               [0, 5000]]
        return And(*[simplify(And(x[i] >= dom[i][0], x[i] <= dom[i][1])) for i in range(len(dom))])

    exp = Experiment("con-sf-2000",
                      bdt_con_2000,
                      successor_con_sf_2000,
                      domain,
                      num_params = 1,
                      num_coefficients = 2,
                      num_partitions = 3,
                      dim = 2,
                      num_initial = 2
                      )
    return exp

def exp_con_sf_5000():
    def domain(x):
        """
            Domain bounding variable values to reachable statespace (only for which values are considered in the conditions, the variables still run over unbounded integers)
        """
        dom = [[0, 5000],
               [0, 12500]]
        return And(*[simplify(And(x[i] >= dom[i][0], x[i] <= dom[i][1])) for i in range(len(dom))])

    exp = Experiment("con-sf-5000",
                      bdt_con_5000,
                      successor_con_sf_5000,
                      domain,
                      num_params = 1,
                      num_coefficients = 2,
                      num_partitions = 3,
                      dim = 2,
                      num_initial = 2
                      )
    return exp

def exp_con_sf_10000():
    def domain(x):
        """
            Domain bounding variable values to reachable statespace (only for which values are considered in the conditions, the variables still run over unbounded integers)
        """
        dom = [[0, 10000],
               [0, 25000]]
        return And(*[simplify(And(x[i] >= dom[i][0], x[i] <= dom[i][1])) for i in range(len(dom))])

    exp = Experiment("con-sf-10000",
                      bdt_con_10000,
                      successor_con_sf_10000,
                      domain,
                      num_params = 1,
                      num_coefficients = 2,
                      num_partitions = 3,
                      dim = 2,
                      num_initial = 5
                      )
    return exp

def exp_con_usf_10():
    def domain(x):
        """
            Domain bounding variable values to reachable statespace (only for which values are considered in the conditions, the variables still run over unbounded integers)
        """
        dom = [[0, 10],
               [0, 20]]
        return And(*[simplify(And(x[i] >= dom[i][0], x[i] <= dom[i][1])) for i in range(len(dom))])

    exp = Experiment("con-usf-10",
                      bdt_con_10,
                      successor_con_usf_10,
                      domain,
                      num_params = 1,
                      num_coefficients = 2,
                      num_partitions = 3,
                      dim = 2,
                      num_initial = 5
                      )
    return exp

def exp_con_usf_100():
    def domain(x):
        """
            Domain bounding variable values to reachable statespace (only for which values are considered in the conditions, the variables still run over unbounded integers)
        """
        dom = [[0, 100],
               [0, 250]]
        return And(*[simplify(And(x[i] >= dom[i][0], x[i] <= dom[i][1])) for i in range(len(dom))])

    exp = Experiment("con-usf-100",
                      bdt_con_100,
                      successor_con_usf_100,
                      domain,
                      num_params = 1,
                      num_coefficients = 2,
                      num_partitions = 3,
                      dim = 2,
                      num_initial = 5
                      )
    return exp

def exp_con_usf_1000():
    def domain(x):
        """
            Domain bounding variable values to reachable statespace (only for which values are considered in the conditions, the variables still run over unbounded integers)
        """
        dom = [[0, 1000],
               [0, 2500]]
        return And(*[simplify(And(x[i] >= dom[i][0], x[i] <= dom[i][1])) for i in range(len(dom))])

    exp = Experiment("con-usf-1000",
                      bdt_con_1000,
                      successor_con_usf_1000,
                      domain,
                      num_params = 1,
                      num_coefficients = 2,
                      num_partitions = 3,
                      dim = 2,
                      num_initial = 5
                      )
    return exp

def exp_con_usf_2000():
    def domain(x):
        """
            Domain bounding variable values to reachable statespace (only for which values are considered in the conditions, the variables still run over unbounded integers)
        """
        dom = [[0, 2000],
               [0, 5000]]
        return And(*[simplify(And(x[i] >= dom[i][0], x[i] <= dom[i][1])) for i in range(len(dom))])

    exp = Experiment("con-usf-2000",
                      bdt_con_2000,
                      successor_con_usf_2000,
                      domain,
                      num_params = 1,
                      num_coefficients = 2,
                      num_partitions = 3,
                      dim = 2,
                      num_initial = 5
                      )
    return exp

def exp_con_usf_5000():
    def domain(x):
        """
            Domain bounding variable values to reachable statespace (only for which values are considered in the conditions, the variables still run over unbounded integers)
        """
        dom = [[0, 5000],
               [0, 12500]]
        return And(*[simplify(And(x[i] >= dom[i][0], x[i] <= dom[i][1])) for i in range(len(dom))])

    exp = Experiment("con-usf-5000",
                      bdt_con_5000,
                      successor_con_usf_5000,
                      domain,
                      num_params = 1,
                      num_coefficients = 2,
                      num_partitions = 3,
                      dim = 2,
                      num_initial = 5
                      )
    return exp

def exp_con_usf_10000():
    def domain(x):
        """
            Domain bounding variable values to reachable statespace (only for which values are considered in the conditions, the variables still run over unbounded integers)
        """
        dom = [[0, 10000],
               [0, 25000]]
        return And(*[simplify(And(x[i] >= dom[i][0], x[i] <= dom[i][1])) for i in range(len(dom))])

    exp = Experiment("con-usf-10000",
                      bdt_con_10000,
                      successor_con_usf_10000,
                      domain,
                      num_params = 1,
                      num_coefficients = 2,
                      num_partitions = 3,
                      dim = 2,
                      num_initial = 5
                      )
    return exp

#run_clock_synch_experiments()