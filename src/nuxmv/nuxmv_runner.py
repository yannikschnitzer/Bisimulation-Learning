"""
    nuXmv exeperiments and command line access.
"""

import subprocess
import os
import multiprocessing
import time

__author__ = "Yannik Schnitzer"
__copyright__ = "Copyright 2024, Yannik Schnitzer"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "yannik.schnitzer@cs.ox.ac.uk"
__status__ = "Experimental - Artifact Evaluation"

class nuXmv_Experiment:
    def __init__(self, name, file, print_res = False):
        self.name = name
        self.file = file
        self.print_res = print_res

def run_cmd(cmd):
    out = subprocess.check_output(cmd, shell = True, text = True, stderr=subprocess.DEVNULL)
    return out

def run_nuXmv_experiment(exp : nuXmv_Experiment, timeout = 500):
        """
            Runs nuXmv with given experiment.
        """
        cmd = "../../nuXmv-2.0.0-Linux/bin/nuXmv -source ../nuXmv-files/" + exp.file
        
        print("------------------------------------")
        print("Running Experiment: ", exp.name)
        
        t1 = time.perf_counter()
        p = multiprocessing.Process(target=run_cmd, name="Runner", args=(cmd, ))
        p.start()
        p.join(timeout)
        t2 = time.perf_counter()
    
        if p.is_alive():
            print("Timeout after",timeout,"seconds")
            p.terminate()
            p.join()

        print("Runtime: ", t2 - t1,"seconds")
        print("------------------------------------")

