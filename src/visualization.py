"""
 Main Classes for CEGIS Procedure of Bisimulation Learning. Contains Learner, Verifier and also one-shot solving without learning.
"""

import time
from utils import *
from experiment import *
from z3 import *
from conditional_termination_succ_trees import *
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap 

__author__ = "Yannik Schnitzer"
__copyright__ = "Copyright 2024, Yannik Schnitzer"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "yannik.schnitzer@cs.ox.ac.uk"
__status__ = "Experimental - Artifact Evaluation"


def predictor(a, classifier, mp, num_params, partitions):
    p = Int("p")
    q = Int("q")
    result = []
    _, tree = classifier(mp, [p,q], num_params, partitions)
    a = a.tolist()
    counter = 0
    for i in a:
        try:
            res = tree.pred([i[0],i[1]])
        except:
            res = -1
        result.append(res)
        counter += 1
    return np.array(result)

def transform_ctx(ctxs, in_view):
    res = []
    for ctx in ctxs:
        new = []
        for comp in ctx:
            dec : IntNumRef = simplify(comp) 
            new.append(dec.as_long())
        if (in_view(new)):
            res.append(np.array(new))
    return np.array(res)
    
def visualize(mp, exp : Experiment, acc, save = False):
    x_min, x_max = -3, 10
    y_min, y_max = -3, 10
    xx, yy = np.meshgrid(np.arange(x_min, x_max, acc), np.arange(y_min, y_max, acc))

    #print(len(np.around(np.c_[xx.ravel(), yy.ravel()], decimals = 3)))
    Z = predictor(np.around(np.c_[xx.ravel(), yy.ravel()], decimals = 3), exp.classifier, mp, exp.num_params, [IntVal(i) for i in range(exp.num_partitions)])
    Z = Z.reshape(xx.shape)

    # Create a colormap for the decision regions
    cmap = ListedColormap(['#FFAAAA', '#FFCCFF','#DFFFFC' ,'#AAFFFF', '#AAAAFF','#BBAAFF','#AADDFF','#DDBBFF','#CCDDFF','#CCCCFF','#FBBCFF','#FBBCCC','#CCBCCC','#FBBAAA','#AAACCC','#DDBDDC','#DDBFFF','#FFFDDC'][:exp.num_partitions])

    # Plot the decision regions
    plt.figure()
    plt.pcolormesh(xx,yy,Z, cmap=cmap)

    def in_view(x):
        return x[0] >= x_min and x[1] >= y_min and x[0] <= x_max and x[1] <= y_max

    # Plot the training data points
    # examples = transform_ctx(ctxs, in_view)
    # plt.scatter(examples[:,0],examples[:,1])
    plt.xlabel('$x$') 
    plt.ylabel('$y$',rotation=0)
    plt.axis('square')
    #plt.title('Decision Regions of Decision Tree Classifier')
    # annotaed = []

    # example_classes = predictor(examples)

    # for i in range(len(examples)):
    #     ex = examples[i]
    #     c = example_classes[i]
    #     if c not in annotaed and in_view(ex):
    #         plt.annotate(c, ex)
    #         annotaed.append(c)
    plt.colorbar(ticks = range(exp.num_partitions))
    if save:
        plt.savefig('./figures/{}_partition.png'.format(exp.name), dpi = 800, bbox_inches='tight')
    else:
        plt.show(block = True)

    