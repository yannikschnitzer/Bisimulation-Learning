"""
    Main file for commandline interface.
"""
import argparse
from conditional_termination_experiments import *
from clock_synchronization_experiments import *
from cpa.CPA_runner import *
from cpa.CPA_experiments import *
from ultimate.ultimate_experiments import *
from nuxmv.nuxmv_experiments import *

__author__ = "Yannik Schnitzer"
__copyright__ = "Copyright 2024, Yannik Schnitzer"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "yannik.schnitzer@cs.ox.ac.uk"
__status__ = "Experimental - Artifact Evaluation"


def main_cond_term():
    print("Running Conditional Termination Benchmarks")
    run_cond_term_experiments()
    print("Experiments ran successfully.")

def main_clock_synch():
    print("Running Conditional Termination Benchmarks")
    run_clock_synch_experiments()
    print("Experiments ran successfully.")

def main_cpa_exps():
    print("Running Conditional Termination Benchmarks with CPA Checker")
    run_cpa_experiments()
    print("Experiments ran successfully.")

def main_nuxmv_cond_term(timeout):
    print("Running Conditional Termination Benchmarks with nuXmv")
    run_nuXmv_experiments_cond(timeout)
    print("Experiments ran successfully.")

def main_nuxmv_sync(timeout):
    print("Running Clock Synchronization Benchmarks with nuXmv")
    run_nuXmv_experiments_sync(timeout)
    print("Experiments ran successfully.")

def main_smoke_test():
    print("Running Smoke Test... Invoking every tool once... \n \n")
    print("CEGIS Smoke Test:")
    run_cond_smoketest()

    print("\n")
    print("Ultimate Automizer Smoke Test:")
    run_ultimate_smoketest()

    print("\n")
    print("CPA Checker Smoke Test:")
    run_cpa_smoketest()

    print("\n")
    print("nuXmv Smoke Test:")
    run_nuXmv_smoketest()

    print("\n")
    print("All smoke tests ran successfully :)")

if __name__ == "__main__":
    parser = argparse.ArgumentParser("CAV 24 Artifact Evaluation for Bisimulation Learning",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-cond","--cond_term", action="store_true", help="Run Conditional Termination Benchmarks")
    parser.add_argument("-sync","--clock_sync", action="store_true" ,help="Run Clock Synchronization Benchmarks")
    parser.add_argument("-v","--verbose", action="store_true" ,help="Print current results at every iteration of the learner (may affect runtime)")
    parser.add_argument("-cpa", "--cpa_checker", action="store_true", help="Run benchmarks with CPA-Checker")
    parser.add_argument("-ult", "--ultimate", action="store_true", help="Run benchmarks with Ultimate Automizer")
    parser.add_argument("-nxcond", "--nuxmv_cond_term", action="store_true", help="Run conditional termination benchmarks with nuXmv")
    parser.add_argument("-nxsync", "--nuxmv_sync", action="store_true", help="Run clock synchronization benchmarks with nuXmv")
    parser.add_argument("-to", "--timeout", help="Set timeout (only for nuXmv)", default=500)
    parser.add_argument("-smoke", "--smoke_test", action="store_true", help="Run smoke test")

    args = parser.parse_args()
    config = vars(args)

    if config['smoke_test']:
        main_smoke_test()
    
    if config['cond_term']:
        main_cond_term()
    
    if config['clock_sync']:
        main_clock_synch()
    
    if config['cpa_checker']:
        run_cpa_experiments()
    
    if config['ultimate']:
        run_ultimate_experiments()

    if config['nuxmv_cond_term']:
        timeout = int(config['timeout'])
        main_nuxmv_cond_term(timeout)

    if config['nuxmv_sync']:
        timeout = int(config['timeout'])
        main_nuxmv_sync(timeout)