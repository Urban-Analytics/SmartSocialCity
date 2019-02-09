'''
Name of class: probability_functions.py
Author: Sedar Olmez
Institute: Leeds Institute for Data Analytics
Date: 09/02/2019

Class description: This class is a sandbox for executing short methods developed
from the material in the pymc3 https://docs.pymc.io/ documentation and Bayesian
Analysis with Python book.
'''
import numpy as np
import pandas as pd
from scipy.stats import norm
from matplotlib import pyplot as plt


def __init__():
    pass


def probability_distribution_scipy(random_variate_index):
    X = norm(0, 1)
    x = X.rvs(random_variate_index)
    return x


def probability_distribution_3by3_graphs():
    mu_params = [-1, 0, 1]
    sd_params = [0.5, 1, 1.5]
    x = np.linspace(-7, 7, 100) #<-- Our curvature in the graphs.
    f, ax = plt.subplots(len(mu_params), len(sd_params), sharex=True, sharey=True)
    for i in range(3):
        for j in range(3):
            mu = mu_params[i] #<-- For each of the mu_params and sd_params (-1, 0.5)...
            sd = sd_params[j]
            '''This line evaluates the probability density function of the
            normal distribution, given the mu and sd parameters for a set of x
            values'''
            y = norm(mu, sd).pdf(x) #<------ y is equal the normalisation of mu, sd variables.
            ax[i,j].plot(x, y) #<-- for the first axis [0, 0] we plot (x, y).
            ax[i,j].plot(0, 0,
            label="$\\mu$ = {:3.2f}\n$\\sigma$ = {:3.2f}".format(mu, sd), alpha=0)
            ax[i,j].legend(fontsize=12) #<--- add the legend to all 6 graphs.
    ax[2,1].set_xlabel('$x$', fontsize=16) #--- add an X below the graph on row 3 column 2.
    ax[1,0].set_ylabel('$pdf(x)$', fontsize=16) #<--- add p(x) to the graph on row 1 column 0.
    plt.tight_layout() #<--- tighten the figure.
    plt.savefig('B04958_01_01.png', dpi=300, figsize=(5.5, 5.5)) #<--- save the figure as a png.
