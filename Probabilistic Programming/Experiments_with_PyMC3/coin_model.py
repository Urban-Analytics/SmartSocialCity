'''
Name of class: coin_model.py
Author: Sedar Olmez
Institute: Leeds Institute for Data Analytics
Date: 09/02/2019

Class description: This class is a sandbox for executing short methods developed
from the material in the pymc3 https://docs.pymc.io/ documentation and Bayesian
Analysis with Python book.
'''


import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm
from scipy.stats import binom


n_params = [1, 2, 4]
p_params = [0.25, 0.5, 0.75]
x = np.arange(0, max(n_params) + 1)
f, ax = plt.subplots(len(n_params), len(p_params), sharex = True,
                    sharey = True, figsize=(8, 7), constrained_layout = True)

def __init__():
    pass


def coin_flip():
    for i in range(3):
        for j in range(3):
            n = n_params[i]
            p = p_params[j]
            y = binom(n = n, p = p).pmf(x)
            ax[i, j].vlines(x, 0, y, colors='b', lw = 5)
            ax[i, j].set_ylim(0, 1)
            ax[i, j].plot(0, 0, label="n = {:3.2f}\np = {:3.2f}".format(n, p), alpha=0)
            ax[i, j].legend(fontsize = 12)
    ax[2, 1].set_xlabel('$\\theta$', fontsize=14)
    ax[1, 0].set_ylabel('$p(y|\\theta)$', fontsize=14)
    ax[0, 0].set_xticks(x)
    plt.show()
