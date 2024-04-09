"""
 Defines and runs Conditional Termination experiments.
"""

from utils import *
from experiment import Experiment
from experiment_runner import *
from conditional_termination_succ_trees import *
from cegis_solver import *
from visualization import *
import numpy as np

__author__ = "Yannik Schnitzer"
__copyright__ = "Copyright 2024, Yannik Schnitzer"
__license__ = "MIT"
__version__ = "1.0.0" 
__email__ = "yannik.schnitzer@cs.ox.ac.uk"
__status__ = "Experimental - Artifact Evaluation"

def run_cond_smoketest():
    run_experiment(exp_term_loop_1(), benchmark_time = True, save_res = True)

def run_cond_term_experiments():
    run_experiment(exp_term_loop_1(), benchmark_time = True, save_res = True)
    run_experiment(exp_term_loop_2(), benchmark_time = True, save_res = True)
    run_experiment(exp_audio_compr(), benchmark_time = True, save_res = True)
    run_experiment(exp_euclid(), benchmark_time = True, vis = True, save_res = True)
    run_experiment(exp_greater(), benchmark_time = True, vis = True, save_res = True)
    run_experiment(exp_smaller(), benchmark_time = True, vis = True, save_res = True)
    run_experiment(exp_conic(), benchmark_time = True, vis = True, save_res = True)
    run_experiment(exp_disjunction(), benchmark_time = True, save_res = True)
    run_experiment(exp_parallel(), benchmark_time = True, save_res = True)
    run_experiment(exp_quadratic(), benchmark_time = True, save_res = True)
    run_experiment(exp_cubic(), benchmark_time = True, save_res = True)
    run_experiment(exp_nlr_cond(), benchmark_time = True, save_res = True)

def domain(x):
    """
        Domain of unbounded integers.
    """
    return True

def exp_term_loop_1():
    def domain(x):
        """
            Domain bounding x[1] to be a boolean (not-terminated / terminated)
        """
        return simplify(And(x[1] >= 0 , x[1] <= 1))

    exp = Experiment("term-loop-1",
                      bdt_term_loop_1,
                      successor_term_loop_1,
                      domain,
                      num_params = 2,
                      num_coefficients = 2,
                      num_partitions = 3,
                      dim = 2,
                      num_initial = 10
                      )
    return exp

def exp_term_loop_2():
    exp = Experiment("term-loop-2",
                      bdt_term_loop_2,
                      successor_term_loop_2,
                      domain,
                      num_params = 1,
                      num_coefficients = 2,
                      num_partitions = 3,
                      dim = 2,
                      num_initial = 10
                      )
    return exp

def exp_audio_compr():
    exp = Experiment("audio-compr",
                      bdt_audio_compr,
                      successor_audio_compr,
                      domain,
                      num_params = 1,
                      num_coefficients = 1,
                      num_partitions = 3,
                      dim = 1,
                      num_initial = 10
                      )
    return exp


def exp_euclid():
    exp = Experiment("euclid",
                      bdt_euclid,
                      successor_euclid,
                      domain,
                      num_params = 2,
                      num_coefficients = 4,
                      num_partitions = 3,
                      dim = 2,
                      num_initial = 10
                      )
    return exp

def exp_greater():
    exp = Experiment("greater",
                      bdt_greater,
                      successor_greater,
                      domain,
                      num_params = 1,
                      num_coefficients = 2,
                      num_partitions = 3,
                      dim = 2,
                      num_initial = 10
                      )
    return exp

def exp_smaller():
    exp = Experiment("smaller",
                      bdt_smaller,
                      successor_smaller,
                      domain,
                      num_params = 1,
                      num_coefficients = 2,
                      num_partitions = 3,
                      dim = 2,
                      num_initial = 10
                      )
    return exp


def exp_conic():
    exp = Experiment("conic",
                      bdt_conic,
                      successor_conic,
                      domain,
                      num_params = 2,
                      num_coefficients = 4,
                      num_partitions = 3,
                      dim = 2,
                      num_initial = 6
                      )
    return exp

def exp_disjunction():
    exp = Experiment("disjunction",
                      bdt_disjunction,
                      successor_disjunction,
                      domain,
                      num_params = 1,
                      num_coefficients = 3,
                      num_partitions = 3,
                      dim = 3,
                      num_initial = 5
                      )
    return exp

def exp_parallel():
    exp = Experiment("parallel",
                      bdt_parallel,
                      successor_parallel,
                      domain,
                      num_params = 2,
                      num_coefficients = 4,
                      num_partitions = 3,
                      dim = 2,
                      num_initial = 10
                      )
    return exp

def exp_quadratic():
    exp = Experiment("quadratic",
                      bdt_quadratic,
                      successor_quadratic,
                      domain,
                      num_params = 2,
                      num_coefficients = 2,
                      num_partitions = 4,
                      dim = 1,
                      num_initial = 10
                      )
    return exp
    
def exp_cubic():
    exp = Experiment("cubic",
                      bdt_cubic,
                      successor_cubic,
                      domain,
                      num_params = 2,
                      num_coefficients = 2,
                      num_partitions = 4,
                      dim = 1,
                      num_initial = 10
                      )
    return exp

def exp_nlr_cond():
    exp = Experiment("nlr_cond",
                      bdt_nlr_cond,
                      successor_nlr_cond,
                      domain,
                      num_params = 2,
                      num_coefficients = 2,
                      num_partitions = 4,
                      dim = 1,
                      num_initial = 10
                      )
    return exp

# run_cond_term_experiments()