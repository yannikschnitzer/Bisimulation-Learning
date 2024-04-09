"""
    Ultimate Automizer experiments and commandline access.
"""

import subprocess
import os
import re

__author__ = "Yannik Schnitzer"
__copyright__ = "Copyright 2024, Yannik Schnitzer"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "yannik.schnitzer@cs.ox.ac.uk"
__status__ = "Experimental - Artifact Evaluation"

class Ultimate_Experiment:
    def __init__(self, name, file, print_res = False):
        self.name = name
        self.file = file
        self.print_res = print_res

def run_ultimate_experiment(exp : Ultimate_Experiment):
        """
            Runs Ultimate with given experiment.
        """
        cmd = "sudo update-java-alternatives --set java-1.11.0-openjdk-amd64 && ../../ultimate/releaseScripts/default/UAutomizer-linux/Ultimate -tc ../../ultimate/releaseScripts/default/UAutomizer-linux/config/AutomizerTermination.xml -i ../C-Programs/" + exp.file
        os.system("")
        print("------------------------------------")
        print("Running Experiment: ", exp.name)
        out = subprocess.check_output(cmd, shell = True, text = True, stderr=subprocess.DEVNULL)
        time_pattern = r"Automizer plugin needed (\d+\.\d+)"
        matches = re.findall(time_pattern, out)
        if matches:
            print("Ultimate Automizer Analysis Time:", matches[0],"")

        if exp.print_res:
            res_pattern = r"TerminationAnalysisResult: (.*)"
            matches = re.findall(res_pattern, out)
            if matches:
                print("Verification result:", matches[0])
        print("------------------------------------")

