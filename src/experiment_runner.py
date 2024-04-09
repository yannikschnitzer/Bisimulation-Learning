"""
 Code for running, profiling and visualizing experiments.
"""

from utils import *
from experiment import Experiment
from cegis_solver import *
from visualization import *
import numpy as np

__author__ = "Yannik Schnitzer"
__copyright__ = "Copyright 2024, Yannik Schnitzer"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "yannik.schnitzer@cs.ox.ac.uk"
__status__ = "Experimental - Artifact Evaluation"

def run_experiment(exp : Experiment, benchmark_time = False, num_reps = 10, type = "cegis", verbose = False, vis = False, save_res = False):
    """
        Run Experiment with given configuration.
    """
    if type == "cegis":
        solver = CEGIS_Solver()
    elif type == "one-shot":
        solver = One_Shot_Solver()

    if not benchmark_time:
        mp, ap, rp = solver.solve_experiment(exp, verbose = verbose)

        if vis:
            draw_quotient(ap)
            visualize(mp, exp, 0.2)
    
    if benchmark_time:
        print("------------------------------------")
        print("Running Experiment: ", exp.name)
        times = []
        for i in range(num_reps):
            # Reset Solver
            if type == "cegis":
                solver = CEGIS_Solver()
            elif type == "one-shot":
                solver = One_Shot_Solver()

            # Solve experiment and track runtime
            t1 = time.process_time()
            mp, ap, rp = solver.solve_experiment(exp, verbose = verbose)
            t2 = time.process_time()
            abstime = t2 - t1
            print("Run {} Abstraction Time: ".format(i + 1), abstime)
            times.append(abstime)

        # Visualize last iteration
        if vis:
            draw_quotient(ap, exp, save = True)
            visualize(mp, exp, 0.2, save = True)

        # Print result of last iteration to file
        if save_res:
            save_results(mp, ap, rp, exp)

        mean = np.mean(times)
        print("---")
        print("Mean Abstraction Time: ", mean)
        print("Standard Deviation: ", np.std(times))
        print("------------------------------------")
            





    


    

