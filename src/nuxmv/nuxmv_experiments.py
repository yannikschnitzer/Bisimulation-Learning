"""
    Runs the nuXmv baseline experiments.
"""

from nuxmv.nuxmv_runner import *

__author__ = "Yannik Schnitzer"
__copyright__ = "Copyright 2024, Yannik Schnitzer"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "yannik.schnitzer@cs.ox.ac.uk"
__status__ = "Experimental - Artifact Evaluation"

def run_nuXmv_smoketest(timeout = 10):
    run_nuXmv_experiment(exp_term_loop_1_term(), timeout)

def run_nuXmv_experiments_cond(timeout = 500):
    run_nuXmv_experiment(exp_term_loop_1_term(), timeout)
    run_nuXmv_experiment(exp_term_loop_1_nonterm(), timeout)
    run_nuXmv_experiment(exp_term_loop_2_term(), timeout)
    run_nuXmv_experiment(exp_term_loop_2_nonterm(), timeout)
    run_nuXmv_experiment(exp_audio_compr_term(), timeout)
    run_nuXmv_experiment(exp_audio_compr_nonterm(), timeout)
    run_nuXmv_experiment(exp_euclid_term(), timeout)
    run_nuXmv_experiment(exp_euclid_nonterm(), timeout)
    run_nuXmv_experiment(exp_greater_term(), timeout)
    run_nuXmv_experiment(exp_greater_nonterm(), timeout)
    run_nuXmv_experiment(exp_smaller_term(), timeout)
    run_nuXmv_experiment(exp_smaller_nonterm(), timeout)
    run_nuXmv_experiment(exp_conic_term(), timeout)
    run_nuXmv_experiment(exp_conic_nonterm(), timeout)
    run_nuXmv_experiment(exp_disjunct(), timeout)
    run_nuXmv_experiment(exp_parallel(), timeout)
    run_nuXmv_experiment(exp_quadratic(), timeout)
    run_nuXmv_experiment(exp_cubic_term(), timeout)
    run_nuXmv_experiment(exp_cubic_nonterm(), timeout)
    run_nuXmv_experiment(exp_non_linear_cond_term(), timeout)
    run_nuXmv_experiment(exp_non_linear_cond_nonterm(), timeout)

def run_nuXmv_experiments_sync(timeout = 500):
    run_nuXmv_experiment(exp_tte_sf_10_g_bdd(), timeout)
    run_nuXmv_experiment(exp_tte_sf_10_g_ic3(), timeout)
    run_nuXmv_experiment(exp_tte_sf_10_gf_bdd(), timeout)
    run_nuXmv_experiment(exp_tte_sf_10_gf_ic3(), timeout)
    run_nuXmv_experiment(exp_tte_sf_100_g_bdd(), timeout)
    run_nuXmv_experiment(exp_tte_sf_100_g_ic3(), timeout)
    run_nuXmv_experiment(exp_tte_sf_100_gf_bdd(), timeout)
    run_nuXmv_experiment(exp_tte_sf_100_gf_ic3(), timeout)
    run_nuXmv_experiment(exp_tte_sf_1000_g_bdd(), timeout)
    run_nuXmv_experiment(exp_tte_sf_1000_g_ic3(), timeout)
    run_nuXmv_experiment(exp_tte_sf_1000_gf_bdd(), timeout)
    run_nuXmv_experiment(exp_tte_sf_1000_gf_ic3(), timeout)
    run_nuXmv_experiment(exp_tte_sf_2000_g_bdd(), timeout)
    run_nuXmv_experiment(exp_tte_sf_2000_g_ic3(), timeout)
    run_nuXmv_experiment(exp_tte_sf_2000_gf_bdd(), timeout)
    run_nuXmv_experiment(exp_tte_sf_2000_gf_ic3(), timeout)
    run_nuXmv_experiment(exp_tte_sf_5000_g_bdd(), timeout)
    run_nuXmv_experiment(exp_tte_sf_5000_g_ic3(), timeout)
    run_nuXmv_experiment(exp_tte_sf_5000_gf_bdd(), timeout)
    run_nuXmv_experiment(exp_tte_sf_5000_gf_ic3(), timeout)
    run_nuXmv_experiment(exp_tte_sf_10000_g_bdd(), timeout)
    run_nuXmv_experiment(exp_tte_sf_10000_g_ic3(), timeout)
    run_nuXmv_experiment(exp_tte_sf_10000_gf_bdd(), timeout)
    run_nuXmv_experiment(exp_tte_sf_10000_gf_ic3(), timeout)

    run_nuXmv_experiment(exp_tte_usf_10_g_bdd(), timeout)
    run_nuXmv_experiment(exp_tte_usf_10_g_ic3(), timeout)
    run_nuXmv_experiment(exp_tte_usf_10_gf_bdd(), timeout)
    run_nuXmv_experiment(exp_tte_usf_10_gf_ic3(), timeout)
    run_nuXmv_experiment(exp_tte_usf_100_g_bdd(), timeout)
    run_nuXmv_experiment(exp_tte_usf_100_g_ic3(), timeout)
    run_nuXmv_experiment(exp_tte_usf_100_gf_bdd(), timeout)
    run_nuXmv_experiment(exp_tte_usf_100_gf_ic3(), timeout)
    run_nuXmv_experiment(exp_tte_usf_1000_g_bdd(), timeout)
    run_nuXmv_experiment(exp_tte_usf_1000_g_ic3(), timeout)
    run_nuXmv_experiment(exp_tte_usf_1000_gf_bdd(), timeout)
    run_nuXmv_experiment(exp_tte_usf_1000_gf_ic3(), timeout)
    run_nuXmv_experiment(exp_tte_usf_2000_g_bdd(), timeout)
    run_nuXmv_experiment(exp_tte_usf_2000_g_ic3(), timeout)
    run_nuXmv_experiment(exp_tte_usf_2000_gf_bdd(), timeout)
    run_nuXmv_experiment(exp_tte_usf_2000_gf_ic3(), timeout)
    run_nuXmv_experiment(exp_tte_usf_5000_g_bdd(), timeout)
    run_nuXmv_experiment(exp_tte_usf_5000_g_ic3(), timeout)
    run_nuXmv_experiment(exp_tte_usf_5000_gf_bdd(), timeout)
    run_nuXmv_experiment(exp_tte_usf_5000_gf_ic3(), timeout)
    run_nuXmv_experiment(exp_tte_usf_10000_g_bdd(), timeout)
    run_nuXmv_experiment(exp_tte_usf_10000_g_ic3(), timeout)
    run_nuXmv_experiment(exp_tte_usf_10000_gf_bdd(), timeout)
    run_nuXmv_experiment(exp_tte_usf_10000_gf_ic3(), timeout)

    run_nuXmv_experiment(exp_con_sf_10_g_bdd(), timeout)
    run_nuXmv_experiment(exp_con_sf_10_g_ic3(), timeout)
    run_nuXmv_experiment(exp_con_sf_10_gf_bdd(), timeout)
    run_nuXmv_experiment(exp_con_sf_10_gf_ic3(), timeout)
    run_nuXmv_experiment(exp_con_sf_100_g_bdd(), timeout)
    run_nuXmv_experiment(exp_con_sf_100_g_ic3(), timeout)
    run_nuXmv_experiment(exp_con_sf_100_gf_bdd(), timeout)
    run_nuXmv_experiment(exp_con_sf_100_gf_ic3(), timeout)
    run_nuXmv_experiment(exp_con_sf_1000_g_bdd(), timeout)
    run_nuXmv_experiment(exp_con_sf_1000_g_ic3(), timeout)
    run_nuXmv_experiment(exp_con_sf_1000_gf_bdd(), timeout)
    run_nuXmv_experiment(exp_con_sf_1000_gf_ic3(), timeout)
    run_nuXmv_experiment(exp_con_sf_2000_g_bdd(), timeout)
    run_nuXmv_experiment(exp_con_sf_2000_g_ic3(), timeout)
    run_nuXmv_experiment(exp_con_sf_2000_gf_bdd(), timeout)
    run_nuXmv_experiment(exp_con_sf_2000_gf_ic3(), timeout)
    run_nuXmv_experiment(exp_con_sf_5000_g_bdd(), timeout)
    run_nuXmv_experiment(exp_con_sf_5000_g_ic3(), timeout)
    run_nuXmv_experiment(exp_con_sf_5000_gf_bdd(), timeout)
    run_nuXmv_experiment(exp_con_sf_5000_gf_ic3(), timeout)
    run_nuXmv_experiment(exp_con_sf_10000_g_bdd(), timeout)
    run_nuXmv_experiment(exp_con_sf_10000_g_ic3(), timeout)
    run_nuXmv_experiment(exp_con_sf_10000_gf_bdd(), timeout)
    run_nuXmv_experiment(exp_con_sf_10000_gf_ic3(), timeout)

    run_nuXmv_experiment(exp_con_usf_10_g_bdd(), timeout)
    run_nuXmv_experiment(exp_con_usf_10_g_ic3(), timeout)
    run_nuXmv_experiment(exp_con_usf_10_gf_bdd(), timeout)
    run_nuXmv_experiment(exp_con_usf_10_gf_ic3(), timeout)
    run_nuXmv_experiment(exp_con_usf_100_g_bdd(), timeout)
    run_nuXmv_experiment(exp_con_usf_100_g_ic3(), timeout)
    run_nuXmv_experiment(exp_con_usf_100_gf_bdd(), timeout)
    run_nuXmv_experiment(exp_con_usf_100_gf_ic3(), timeout)
    run_nuXmv_experiment(exp_con_usf_1000_g_bdd(), timeout)
    run_nuXmv_experiment(exp_con_usf_1000_g_ic3(), timeout)
    run_nuXmv_experiment(exp_con_usf_1000_gf_bdd(), timeout)
    run_nuXmv_experiment(exp_con_usf_1000_gf_ic3(), timeout)
    run_nuXmv_experiment(exp_con_usf_2000_g_bdd(), timeout)
    run_nuXmv_experiment(exp_con_usf_2000_g_ic3(), timeout)
    run_nuXmv_experiment(exp_con_usf_2000_gf_bdd(), timeout)
    run_nuXmv_experiment(exp_con_usf_2000_gf_ic3(), timeout)
    run_nuXmv_experiment(exp_con_usf_5000_g_bdd(), timeout)
    run_nuXmv_experiment(exp_con_usf_5000_g_ic3(), timeout)
    run_nuXmv_experiment(exp_con_usf_5000_gf_bdd(), timeout)
    run_nuXmv_experiment(exp_con_usf_5000_gf_ic3(), timeout)
    run_nuXmv_experiment(exp_con_usf_10000_g_bdd(), timeout)
    run_nuXmv_experiment(exp_con_usf_10000_g_ic3(), timeout)
    run_nuXmv_experiment(exp_con_usf_10000_gf_bdd(), timeout)
    run_nuXmv_experiment(exp_con_usf_10000_gf_ic3(), timeout)



def exp_term_loop_1_term():
    exp = nuXmv_Experiment(
        "term-loop-1-term",
        "source_term-loop-1-term.txt"
    )
    return exp

def exp_term_loop_1_nonterm():
    exp = nuXmv_Experiment(
        "term-loop-1-nonterm",
        "source_term-loop-1-nonterm.txt"
    )
    return exp

def exp_term_loop_2_term():
    exp = nuXmv_Experiment(
        "term-loop-2-term",
        "source_term-loop-2-term.txt"
    )
    return exp

def exp_term_loop_2_nonterm():
    exp = nuXmv_Experiment(
        "term-loop-2-nonterm",
        "source_term-loop-2-nonterm.txt"
    )
    return exp

def exp_audio_compr_term():
    exp = nuXmv_Experiment(
        "audio-compr-term",
        "source_audio-compr-term.txt"
    )
    return exp

def exp_audio_compr_nonterm():
    exp = nuXmv_Experiment(
        "audio-compr-nonterm",
        "source_audio-compr-nonterm.txt"
    )
    return exp

def exp_euclid_term():
    exp = nuXmv_Experiment(
        "euclid-term",
        "source_euclid-term.txt"
    )
    return exp

def exp_euclid_nonterm():
    exp = nuXmv_Experiment(
        "euclid-nonterm",
        "source_euclid-nonterm.txt"
    )
    return exp

def exp_greater_term():
    exp = nuXmv_Experiment(
        "greater-term",
        "source_greater-term.txt"
    )
    return exp

def exp_greater_nonterm():
    exp = nuXmv_Experiment(
        "greater-nonterm",
        "source_greater-nonterm.txt"
    )
    return exp

def exp_smaller_term():
    exp = nuXmv_Experiment(
        "smaller-term",
        "source_smaller-term.txt"
    )
    return exp

def exp_smaller_nonterm():
    exp = nuXmv_Experiment(
        "smaller-nonterm",
        "source_smaller-nonterm.txt"
    )
    return exp

def exp_conic_term():
    exp = nuXmv_Experiment(
        "conic-term",
        "source_conic-term.txt"
    )
    return exp

def exp_conic_nonterm():
    exp = nuXmv_Experiment(
        "conic-nonterm",
        "source_conic-nonterm.txt"
    )
    return exp

def exp_disjunct():
    exp = nuXmv_Experiment(
        "disjunction",
        "source_disjunction.txt"
    )
    return exp

def exp_parallel():
    exp = nuXmv_Experiment(
        "parallel",
        "source_parallel.txt"
    )
    return exp

def exp_quadratic():
    exp = nuXmv_Experiment(
        "quadratic",
        "source_quadratic.txt"
    )
    return exp

def exp_cubic_term():
    exp = nuXmv_Experiment(
        "cubic-term",
        "source_cubic-term.txt"
    )
    return exp

def exp_cubic_nonterm():
    exp = nuXmv_Experiment(
        "cubic-nonterm",
        "source_cubic-nonterm.txt"
    )
    return exp


def exp_non_linear_cond_term():
    exp = nuXmv_Experiment(
        "non-linear-cond-term",
        "source_non-linear-cond-term.txt"
    )
    return exp

def exp_non_linear_cond_nonterm():
    exp = nuXmv_Experiment(
        "non-linear-cond-nonterm",
        "source_non-linear-cond-nonterm.txt"
    )
    return exp

def exp_tte_sf_10_g_bdd():
    exp = nuXmv_Experiment(
        "tte-sf-10-G-BDD",
        "synch_tte/source_tte_sf_10_g_bdd.txt"
    )
    return exp

def exp_tte_sf_10_g_ic3():
    exp = nuXmv_Experiment(
        "tte-sf-10-G-IC3",
        "synch_tte/source_tte_sf_10_g_ic3.txt"
    )
    return exp

def exp_tte_sf_10_gf_bdd():
    exp = nuXmv_Experiment(
        "tte-sf-10-GF-BDD",
        "synch_tte/source_tte_sf_10_gf_bdd.txt"
    )
    return exp

def exp_tte_sf_10_gf_ic3():
    exp = nuXmv_Experiment(
        "tte-sf-10-GF-IC3",
        "synch_tte/source_tte_sf_10_gf_ic3.txt"
    )
    return exp



def exp_tte_sf_100_g_bdd():
    exp = nuXmv_Experiment(
        "tte-sf-100-G-BDD",
        "synch_tte/source_tte_sf_100_g_bdd.txt"
    )
    return exp

def exp_tte_sf_100_g_ic3():
    exp = nuXmv_Experiment(
        "tte-sf-100-G-IC3",
        "synch_tte/source_tte_sf_100_g_ic3.txt"
    )
    return exp

def exp_tte_sf_100_gf_bdd():
    exp = nuXmv_Experiment(
        "tte-sf-100-GF-BDD",
        "synch_tte/source_tte_sf_100_gf_bdd.txt"
    )
    return exp

def exp_tte_sf_100_gf_ic3():
    exp = nuXmv_Experiment(
        "tte-sf-100-GF-IC3",
        "synch_tte/source_tte_sf_100_gf_ic3.txt"
    )
    return exp

def exp_tte_sf_1000_g_bdd():
    exp = nuXmv_Experiment(
        "tte-sf-1000-G-BDD",
        "synch_tte/source_tte_sf_1000_g_bdd.txt"
    )
    return exp

def exp_tte_sf_1000_g_ic3():
    exp = nuXmv_Experiment(
        "tte-sf-1000-G-IC3",
        "synch_tte/source_tte_sf_1000_g_ic3.txt"
    )
    return exp

def exp_tte_sf_1000_gf_bdd():
    exp = nuXmv_Experiment(
        "tte-sf-1000-GF-BDD",
        "synch_tte/source_tte_sf_1000_gf_bdd.txt"
    )
    return exp

def exp_tte_sf_1000_gf_ic3():
    exp = nuXmv_Experiment(
        "tte-sf-1000-GF-IC3",
        "synch_tte/source_tte_sf_1000_gf_ic3.txt"
    )
    return exp

def exp_tte_sf_2000_g_bdd():
    exp = nuXmv_Experiment(
        "tte-sf-2000-G-BDD",
        "synch_tte/source_tte_sf_2000_g_bdd.txt"
    )
    return exp

def exp_tte_sf_2000_g_ic3():
    exp = nuXmv_Experiment(
        "tte-sf-2000-G-IC3",
        "synch_tte/source_tte_sf_2000_g_ic3.txt"
    )
    return exp

def exp_tte_sf_2000_gf_bdd():
    exp = nuXmv_Experiment(
        "tte-sf-2000-GF-BDD",
        "synch_tte/source_tte_sf_2000_gf_bdd.txt"
    )
    return exp

def exp_tte_sf_2000_gf_ic3():
    exp = nuXmv_Experiment(
        "tte-sf-2000-GF-IC3",
        "synch_tte/source_tte_sf_2000_gf_ic3.txt"
    )
    return exp

def exp_tte_sf_5000_g_bdd():
    exp = nuXmv_Experiment(
        "tte-sf-5000-G-BDD",
        "synch_tte/source_tte_sf_5000_g_bdd.txt"
    )
    return exp

def exp_tte_sf_5000_g_ic3():
    exp = nuXmv_Experiment(
        "tte-sf-5000-G-IC3",
        "synch_tte/source_tte_sf_5000_g_ic3.txt"
    )
    return exp

def exp_tte_sf_5000_gf_bdd():
    exp = nuXmv_Experiment(
        "tte-sf-5000-GF-BDD",
        "synch_tte/source_tte_sf_5000_gf_bdd.txt"
    )
    return exp

def exp_tte_sf_5000_gf_ic3():
    exp = nuXmv_Experiment(
        "tte-sf-5000-GF-IC3",
        "synch_tte/source_tte_sf_5000_gf_ic3.txt"
    )
    return exp

def exp_tte_sf_10000_g_bdd():
    exp = nuXmv_Experiment(
        "tte-sf-10000-G-BDD",
        "synch_tte/source_tte_sf_10000_g_bdd.txt"
    )
    return exp

def exp_tte_sf_10000_g_ic3():
    exp = nuXmv_Experiment(
        "tte-sf-10000-G-IC3",
        "synch_tte/source_tte_sf_10000_g_ic3.txt"
    )
    return exp

def exp_tte_sf_10000_gf_bdd():
    exp = nuXmv_Experiment(
        "tte-sf-10000-GF-BDD",
        "synch_tte/source_tte_sf_10000_gf_bdd.txt"
    )
    return exp

def exp_tte_sf_10000_gf_ic3():
    exp = nuXmv_Experiment(
        "tte-sf-10000-GF-IC3",
        "synch_tte/source_tte_sf_10000_gf_ic3.txt"
    )
    return exp



def exp_tte_usf_10_g_bdd():
    exp = nuXmv_Experiment(
        "tte-usf-10-G-BDD",
        "synch_tte/source_tte_usf_10_g_bdd.txt"
    )
    return exp

def exp_tte_usf_10_g_ic3():
    exp = nuXmv_Experiment(
        "tte-usf-10-G-IC3",
        "synch_tte/source_tte_usf_10_g_ic3.txt"
    )
    return exp

def exp_tte_usf_10_gf_bdd():
    exp = nuXmv_Experiment(
        "tte-usf-10-GF-BDD",
        "synch_tte/source_tte_usf_10_gf_bdd.txt"
    )
    return exp

def exp_tte_usf_10_gf_ic3():
    exp = nuXmv_Experiment(
        "tte-usf-10-GF-IC3",
        "synch_tte/source_tte_usf_10_gf_ic3.txt"
    )
    return exp

def exp_tte_usf_100_g_bdd():
    exp = nuXmv_Experiment(
        "tte-usf-100-G-BDD",
        "synch_tte/source_tte_usf_100_g_bdd.txt"
    )
    return exp

def exp_tte_usf_100_g_ic3():
    exp = nuXmv_Experiment(
        "tte-usf-100-G-IC3",
        "synch_tte/source_tte_usf_100_g_ic3.txt"
    )
    return exp

def exp_tte_usf_100_gf_bdd():
    exp = nuXmv_Experiment(
        "tte-usf-100-GF-BDD",
        "synch_tte/source_tte_usf_100_gf_bdd.txt"
    )
    return exp

def exp_tte_usf_100_gf_ic3():
    exp = nuXmv_Experiment(
        "tte-usf-100-GF-IC3",
        "synch_tte/source_tte_usf_100_gf_ic3.txt"
    )
    return exp

def exp_tte_usf_1000_g_bdd():
    exp = nuXmv_Experiment(
        "tte-usf-1000-G-BDD",
        "synch_tte/source_tte_usf_1000_g_bdd.txt"
    )
    return exp

def exp_tte_usf_1000_g_ic3():
    exp = nuXmv_Experiment(
        "tte-usf-1000-G-IC3",
        "synch_tte/source_tte_usf_1000_g_ic3.txt"
    )
    return exp

def exp_tte_usf_1000_gf_bdd():
    exp = nuXmv_Experiment(
        "tte-usf-1000-GF-BDD",
        "synch_tte/source_tte_usf_1000_gf_bdd.txt"
    )
    return exp

def exp_tte_usf_1000_gf_ic3():
    exp = nuXmv_Experiment(
        "tte-usf-1000-GF-IC3",
        "synch_tte/source_tte_usf_1000_gf_ic3.txt"
    )
    return exp

def exp_tte_usf_2000_g_bdd():
    exp = nuXmv_Experiment(
        "tte-usf-2000-G-BDD",
        "synch_tte/source_tte_usf_2000_g_bdd.txt"
    )
    return exp

def exp_tte_usf_2000_g_ic3():
    exp = nuXmv_Experiment(
        "tte-usf-2000-G-IC3",
        "synch_tte/source_tte_usf_2000_g_ic3.txt"
    )
    return exp

def exp_tte_usf_2000_gf_bdd():
    exp = nuXmv_Experiment(
        "tte-usf-2000-GF-BDD",
        "synch_tte/source_tte_usf_2000_gf_bdd.txt"
    )
    return exp

def exp_tte_usf_2000_gf_ic3():
    exp = nuXmv_Experiment(
        "tte-usf-2000-GF-IC3",
        "synch_tte/source_tte_usf_2000_gf_ic3.txt"
    )
    return exp

def exp_tte_usf_5000_g_bdd():
    exp = nuXmv_Experiment(
        "tte-usf-5000-G-BDD",
        "synch_tte/source_tte_usf_5000_g_bdd.txt"
    )
    return exp

def exp_tte_usf_5000_g_ic3():
    exp = nuXmv_Experiment(
        "tte-usf-5000-G-IC3",
        "synch_tte/source_tte_usf_5000_g_ic3.txt"
    )
    return exp

def exp_tte_usf_5000_gf_bdd():
    exp = nuXmv_Experiment(
        "tte-usf-5000-GF-BDD",
        "synch_tte/source_tte_usf_5000_gf_bdd.txt"
    )
    return exp

def exp_tte_usf_5000_gf_ic3():
    exp = nuXmv_Experiment(
        "tte-usf-5000-GF-IC3",
        "synch_tte/source_tte_usf_5000_gf_ic3.txt"
    )
    return exp

def exp_tte_usf_10000_g_bdd():
    exp = nuXmv_Experiment(
        "tte-usf-10000-G-BDD",
        "synch_tte/source_tte_usf_10000_g_bdd.txt"
    )
    return exp

def exp_tte_usf_10000_g_ic3():
    exp = nuXmv_Experiment(
        "tte-usf-10000-G-IC3",
        "synch_tte/source_tte_usf_10000_g_ic3.txt"
    )
    return exp

def exp_tte_usf_10000_gf_bdd():
    exp = nuXmv_Experiment(
        "tte-usf-10000-GF-BDD",
        "synch_tte/source_tte_usf_10000_gf_bdd.txt"
    )
    return exp

def exp_tte_usf_10000_gf_ic3():
    exp = nuXmv_Experiment(
        "tte-usf-10000-GF-IC3",
        "synch_tte/source_tte_usf_10000_gf_ic3.txt"
    )
    return exp


def exp_con_sf_10_g_bdd():
    exp = nuXmv_Experiment(
        "con-sf-10-G-BDD",
        "synch_tte/source_con_sf_10_g_bdd.txt"
    )
    return exp

def exp_con_sf_10_g_ic3():
    exp = nuXmv_Experiment(
        "con-sf-10-G-IC3",
        "synch_tte/source_con_sf_10_g_ic3.txt"
    )
    return exp

def exp_con_sf_10_gf_bdd():
    exp = nuXmv_Experiment(
        "con-sf-10-GF-BDD",
        "synch_tte/source_con_sf_10_gf_bdd.txt"
    )
    return exp

def exp_con_sf_10_gf_ic3():
    exp = nuXmv_Experiment(
        "con-sf-10-GF-IC3",
        "synch_tte/source_con_sf_10_gf_ic3.txt"
    )
    return exp



def exp_con_sf_100_g_bdd():
    exp = nuXmv_Experiment(
        "con-sf-100-G-BDD",
        "synch_tte/source_con_sf_100_g_bdd.txt"
    )
    return exp

def exp_con_sf_100_g_ic3():
    exp = nuXmv_Experiment(
        "con-sf-100-G-IC3",
        "synch_tte/source_con_sf_100_g_ic3.txt"
    )
    return exp

def exp_con_sf_100_gf_bdd():
    exp = nuXmv_Experiment(
        "con-sf-100-GF-BDD",
        "synch_tte/source_con_sf_100_gf_bdd.txt"
    )
    return exp

def exp_con_sf_100_gf_ic3():
    exp = nuXmv_Experiment(
        "con-sf-100-GF-IC3",
        "synch_tte/source_con_sf_100_gf_ic3.txt"
    )
    return exp

def exp_con_sf_1000_g_bdd():
    exp = nuXmv_Experiment(
        "con-sf-1000-G-BDD",
        "synch_tte/source_con_sf_1000_g_bdd.txt"
    )
    return exp

def exp_con_sf_1000_g_ic3():
    exp = nuXmv_Experiment(
        "con-sf-1000-G-IC3",
        "synch_tte/source_con_sf_1000_g_ic3.txt"
    )
    return exp

def exp_con_sf_1000_gf_bdd():
    exp = nuXmv_Experiment(
        "con-sf-1000-GF-BDD",
        "synch_tte/source_con_sf_1000_gf_bdd.txt"
    )
    return exp

def exp_con_sf_1000_gf_ic3():
    exp = nuXmv_Experiment(
        "con-sf-1000-GF-IC3",
        "synch_tte/source_con_sf_1000_gf_ic3.txt"
    )
    return exp

def exp_con_sf_2000_g_bdd():
    exp = nuXmv_Experiment(
        "con-sf-2000-G-BDD",
        "synch_tte/source_con_sf_2000_g_bdd.txt"
    )
    return exp

def exp_con_sf_2000_g_ic3():
    exp = nuXmv_Experiment(
        "con-sf-2000-G-IC3",
        "synch_tte/source_con_sf_2000_g_ic3.txt"
    )
    return exp

def exp_con_sf_2000_gf_bdd():
    exp = nuXmv_Experiment(
        "con-sf-2000-GF-BDD",
        "synch_tte/source_con_sf_2000_gf_bdd.txt"
    )
    return exp

def exp_con_sf_2000_gf_ic3():
    exp = nuXmv_Experiment(
        "con-sf-2000-GF-IC3",
        "synch_tte/source_con_sf_2000_gf_ic3.txt"
    )
    return exp

def exp_con_sf_5000_g_bdd():
    exp = nuXmv_Experiment(
        "con-sf-5000-G-BDD",
        "synch_tte/source_con_sf_5000_g_bdd.txt"
    )
    return exp

def exp_con_sf_5000_g_ic3():
    exp = nuXmv_Experiment(
        "con-sf-5000-G-IC3",
        "synch_tte/source_con_sf_5000_g_ic3.txt"
    )
    return exp

def exp_con_sf_5000_gf_bdd():
    exp = nuXmv_Experiment(
        "con-sf-5000-GF-BDD",
        "synch_tte/source_con_sf_5000_gf_bdd.txt"
    )
    return exp

def exp_con_sf_5000_gf_ic3():
    exp = nuXmv_Experiment(
        "con-sf-5000-GF-IC3",
        "synch_tte/source_con_sf_5000_gf_ic3.txt"
    )
    return exp

def exp_con_sf_10000_g_bdd():
    exp = nuXmv_Experiment(
        "con-sf-10000-G-BDD",
        "synch_tte/source_con_sf_10000_g_bdd.txt"
    )
    return exp

def exp_con_sf_10000_g_ic3():
    exp = nuXmv_Experiment(
        "con-sf-10000-G-IC3",
        "synch_tte/source_con_sf_10000_g_ic3.txt"
    )
    return exp

def exp_con_sf_10000_gf_bdd():
    exp = nuXmv_Experiment(
        "con-sf-10000-GF-BDD",
        "synch_tte/source_con_sf_10000_gf_bdd.txt"
    )
    return exp

def exp_con_sf_10000_gf_ic3():
    exp = nuXmv_Experiment(
        "con-sf-10000-GF-IC3",
        "synch_tte/source_con_sf_10000_gf_ic3.txt"
    )
    return exp


def exp_con_usf_10_g_bdd():
    exp = nuXmv_Experiment(
        "con-usf-10-G-BDD",
        "synch_tte/source_con_usf_10_g_bdd.txt"
    )
    return exp

def exp_con_usf_10_g_ic3():
    exp = nuXmv_Experiment(
        "con-usf-10-G-IC3",
        "synch_tte/source_con_usf_10_g_ic3.txt"
    )
    return exp

def exp_con_usf_10_gf_bdd():
    exp = nuXmv_Experiment(
        "con-usf-10-GF-BDD",
        "synch_tte/source_con_usf_10_gf_bdd.txt"
    )
    return exp

def exp_con_usf_10_gf_ic3():
    exp = nuXmv_Experiment(
        "con-usf-10-GF-IC3",
        "synch_tte/source_con_usf_10_gf_ic3.txt"
    )
    return exp



def exp_con_usf_100_g_bdd():
    exp = nuXmv_Experiment(
        "con-usf-100-G-BDD",
        "synch_tte/source_con_usf_100_g_bdd.txt"
    )
    return exp

def exp_con_usf_100_g_ic3():
    exp = nuXmv_Experiment(
        "con-usf-100-G-IC3",
        "synch_tte/source_con_usf_100_g_ic3.txt"
    )
    return exp

def exp_con_usf_100_gf_bdd():
    exp = nuXmv_Experiment(
        "con-usf-100-GF-BDD",
        "synch_tte/source_con_usf_100_gf_bdd.txt"
    )
    return exp

def exp_con_usf_100_gf_ic3():
    exp = nuXmv_Experiment(
        "con-usf-100-GF-IC3",
        "synch_tte/source_con_usf_100_gf_ic3.txt"
    )
    return exp

def exp_con_usf_1000_g_bdd():
    exp = nuXmv_Experiment(
        "con-usf-1000-G-BDD",
        "synch_tte/source_con_usf_1000_g_bdd.txt"
    )
    return exp

def exp_con_usf_1000_g_ic3():
    exp = nuXmv_Experiment(
        "con-usf-1000-G-IC3",
        "synch_tte/source_con_usf_1000_g_ic3.txt"
    )
    return exp

def exp_con_usf_1000_gf_bdd():
    exp = nuXmv_Experiment(
        "con-usf-1000-GF-BDD",
        "synch_tte/source_con_usf_1000_gf_bdd.txt"
    )
    return exp

def exp_con_usf_1000_gf_ic3():
    exp = nuXmv_Experiment(
        "con-usf-1000-GF-IC3",
        "synch_tte/source_con_usf_1000_gf_ic3.txt"
    )
    return exp

def exp_con_usf_2000_g_bdd():
    exp = nuXmv_Experiment(
        "con-usf-2000-G-BDD",
        "synch_tte/source_con_usf_2000_g_bdd.txt"
    )
    return exp

def exp_con_usf_2000_g_ic3():
    exp = nuXmv_Experiment(
        "con-usf-2000-G-IC3",
        "synch_tte/source_con_usf_2000_g_ic3.txt"
    )
    return exp

def exp_con_usf_2000_gf_bdd():
    exp = nuXmv_Experiment(
        "con-usf-2000-GF-BDD",
        "synch_tte/source_con_usf_2000_gf_bdd.txt"
    )
    return exp

def exp_con_usf_2000_gf_ic3():
    exp = nuXmv_Experiment(
        "con-usf-2000-GF-IC3",
        "synch_tte/source_con_usf_2000_gf_ic3.txt"
    )
    return exp

def exp_con_usf_5000_g_bdd():
    exp = nuXmv_Experiment(
        "con-usf-5000-G-BDD",
        "synch_tte/source_con_usf_5000_g_bdd.txt"
    )
    return exp

def exp_con_usf_5000_g_ic3():
    exp = nuXmv_Experiment(
        "con-usf-5000-G-IC3",
        "synch_tte/source_con_usf_5000_g_ic3.txt"
    )
    return exp

def exp_con_usf_5000_gf_bdd():
    exp = nuXmv_Experiment(
        "con-usf-5000-GF-BDD",
        "synch_tte/source_con_usf_5000_gf_bdd.txt"
    )
    return exp

def exp_con_usf_5000_gf_ic3():
    exp = nuXmv_Experiment(
        "con-usf-5000-GF-IC3",
        "synch_tte/source_con_usf_5000_gf_ic3.txt"
    )
    return exp

def exp_con_usf_10000_g_bdd():
    exp = nuXmv_Experiment(
        "con-usf-10000-G-BDD",
        "synch_tte/source_con_usf_10000_g_bdd.txt"
    )
    return exp

def exp_con_usf_10000_g_ic3():
    exp = nuXmv_Experiment(
        "con-usf-10000-G-IC3",
        "synch_tte/source_con_usf_10000_g_ic3.txt"
    )
    return exp

def exp_con_usf_10000_gf_bdd():
    exp = nuXmv_Experiment(
        "con-usf-10000-GF-BDD",
        "synch_tte/source_con_usf_10000_gf_bdd.txt"
    )
    return exp

def exp_con_usf_10000_gf_ic3():
    exp = nuXmv_Experiment(
        "con-usf-10000-GF-IC3",
        "synch_tte/source_con_usf_10000_gf_ic3.txt"
    )
    return exp
