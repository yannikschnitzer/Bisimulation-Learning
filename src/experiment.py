"""
    Experiment Class 
"""

__author__ = "Yannik Schnitzer"
__copyright__ = "Copyright 2024, Yannik Schnitzer"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "yannik.schnitzer@cs.ox.ac.uk"
__status__ = "Experimental - Artifact Evaluation"


class Experiment:
    """
     Class holding all information for an experiment.
     Args:

    """
    def __init__(self, name, classifier, successor, domain, num_params, num_coefficients, num_partitions, dim, num_initial = 10):
        self.name = name
        self.classifier = classifier
        self.successor = successor
        self.domain = domain
        self.num_params = num_params
        self.num_coefficients = num_coefficients
        self.num_partitions = num_partitions
        self.dim = dim
        self.num_initial = num_initial

    def __str__(self):
        str = ""
        str += "Experiment: " + self.name + "\n"
        
        return str