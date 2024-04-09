"""
    Runs the Ultimate Automizer baseline experiments.
"""

from ultimate.ultimate_runner import *

__author__ = "Yannik Schnitzer"
__copyright__ = "Copyright 2024, Yannik Schnitzer"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "yannik.schnitzer@cs.ox.ac.uk"
__status__ = "Experimental - Artifact Evaluation"

def run_ultimate_smoketest():
    run_ultimate_experiment(exp_term_loop_1_term())

def run_ultimate_experiments():
    run_ultimate_experiment(exp_term_loop_1_term())
    run_ultimate_experiment(exp_term_loop_1_nonterm())
    run_ultimate_experiment(exp_term_loop_2_term())
    run_ultimate_experiment(exp_term_loop_2_nonterm())
    run_ultimate_experiment(exp_audio_compr_term())
    run_ultimate_experiment(exp_audio_compr_nonterm())
    run_ultimate_experiment(exp_euclid_term())
    run_ultimate_experiment(exp_euclid_nonterm())
    run_ultimate_experiment(exp_greater_term())
    run_ultimate_experiment(exp_greater_nonterm())
    run_ultimate_experiment(exp_smaller_term())
    run_ultimate_experiment(exp_smaller_nonterm())
    run_ultimate_experiment(exp_conic_term())
    run_ultimate_experiment(exp_conic_nonterm())
    run_ultimate_experiment(exp_disjunction_term())
    run_ultimate_experiment(exp_parallel_term())
    run_ultimate_experiment(exp_quadratic_term())
    run_ultimate_experiment(exp_cubic_term())
    run_ultimate_experiment(exp_cubic_nonterm())
    run_ultimate_experiment(exp_nlr_cond_term())
    run_ultimate_experiment(exp_nlr_cond_nonterm())

def exp_term_loop_1_term():
    exp = Ultimate_Experiment(
        "term-loop-1-term",
        "term-loop-1-term.c"
    )
    return exp

def exp_term_loop_1_nonterm():
    exp = Ultimate_Experiment(
        "term-loop-1-nonterm",
        "term-loop-1-nonterm.c"
    )
    return exp

def exp_term_loop_2_term():
    exp = Ultimate_Experiment(
        "term-loop-2-term",
        "term-loop-2-term.c"
    )
    return exp

def exp_term_loop_2_nonterm():
    exp = Ultimate_Experiment(
        "term-loop-2-nonterm",
        "term-loop-2-nonterm.c"
    )
    return exp

def exp_audio_compr_term():
    exp = Ultimate_Experiment(
        "audio-compr-term",
        "audio_compression-term.c",
    )
    return exp

def exp_audio_compr_nonterm():
    exp = Ultimate_Experiment(
        "audio-compr-nonterm",
        "audio_compression-nonterm.c",
    )
    return exp

def exp_euclid_term():
    exp = Ultimate_Experiment(
        "euclid-term",
        "euclid-term.c",
    )
    return exp

def exp_euclid_nonterm():
    exp = Ultimate_Experiment(
        "euclid-nonterm",
        "euclid-nonterm.c"
    )
    return exp

def exp_greater_term():
    exp = Ultimate_Experiment(
        "greater-term",
        "greater-term.c"
    )
    return exp

def exp_greater_nonterm():
    exp = Ultimate_Experiment(
        "greater-nonterm",
        "greater-nonterm.c"
    )
    return exp

def exp_smaller_term():
    exp = Ultimate_Experiment(
        "smaller-term",
        "smaller-term.c"
    )
    return exp

def exp_smaller_nonterm():
    exp = Ultimate_Experiment(
        "smaller-nonterm",
        "smaller-nonterm.c"
    )
    return exp

def exp_conic_term():
    exp = Ultimate_Experiment(
        "conic-term",
        "conic-term.c",
        print_res=True
    )
    return exp

def exp_conic_nonterm():
    exp = Ultimate_Experiment(
        "conic-nonterm",
        "conic-nonterm.c"
    )
    return exp

def exp_disjunction_term():
    exp = Ultimate_Experiment(
        "disjunction-term",
        "disjunction-term.c"
    )
    return exp

def exp_parallel_term():
    exp = Ultimate_Experiment(
        "parallel-term",
        "parallel.c"
    )
    return exp

def exp_quadratic_term():
    exp = Ultimate_Experiment(
        "quadratic-term",
        "quadratic.c",
        print_res=True
    )
    return exp

def exp_cubic_term():
    exp = Ultimate_Experiment(
        "cubic-term",
        "cubic-term.c",
        print_res=True
    )
    return exp


def exp_cubic_nonterm():
    exp = Ultimate_Experiment(
        "cubic-nonterm",
        "cubic-nonterm.c"
    )
    return exp


def exp_nlr_cond_term():
    exp = Ultimate_Experiment(
        "nlr-cond-term",
        "non-linear-cond-term.c",
        print_res=True
    )
    return exp

def exp_nlr_cond_nonterm():
    exp = Ultimate_Experiment(
        "nlr-cond-nonterm",
        "non-linear-cond-nonterm.c"
    )
    return exp