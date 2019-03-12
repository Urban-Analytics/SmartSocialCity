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
from scipy.stats import beta
from matplotlib import pyplot as plt
import arviz as az

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
    plt.show() #<--- show the figure.


def beta_distribution_priori():
    parameters = [0.5, 1, 2 ,3]
    x = np.linspace(0, 1, 100)
    f, ax = plt.subplots(len(parameters), len(parameters), sharex = True, sharey = True,
                        figsize = (8, 7), constrained_layout = True)
    for i in range(4):
        for j in range(4):
            a = parameters[i]
            b = parameters[j]
            y = beta(a, b).pdf(x)
            ax[i, j].plot(x, y)
            ax[i,j].plot(0, 0, label="$\\alpha$ = {:3.2f}\n$\\beta$ = {:3.2f}".format(a, b), alpha=0)
            ax[i, j].legend()
            ax[1, 0].set_yticks([])
            ax[1, 0].set_xticks([0, 0.5, 1])
            f.text(0.5, 0.05, '$\\theta$', ha = 'center')
            f.text(0.07, 0.5, '$p\\theta$', va = 'center', rotation = 0)
            plt.show()

'''
def posterior_plot():
    plt.figure(figsize=(10, 8))
    n_trials = [0, 1, 2, 3, 4, 8, 16, 32, 50, 150]
    data = [0, 1, 1, 1, 1, 4, 6, 9, 13, 48]
    theta_real = 0.35

    beta_params = [(1, 1), (20, 20), (1, 4)]
    dist = beta
    x = np.linspace(0, 1, 200)

    for idx, N in enumerate(n_trials):
        if idx == 0:
            plt.subplot(4, 3, 2)
            plt.xlabel('$\\theta$')
        else:
            plt.subplot(4, 3, idx+3)
            plt.xticks([])
        y = data[idx]
        for (a_priori, b_priori) in beta_params:
            p_theta_given_y = dist.pdf(x, a_priori + y, b_priori + N - y)
            plt.fill_between(x, 0, p_theta_given_y, alpha = 0.7)

        plt.axvline(theta_real, ymax = 0.3, color = 'k')
        plt.plot(0, 0, label = f'{N:4d} trials\n{y:4d} heads', alpha = 0)
        plt.xlim(0, 1)
        plt.ylim(0, 12)
        plt.legend()
        plt.yticks([])
    plt.tight_layout()
    plt.show()'''

def highest_posterior_density(random_val):
    np.random.seed(random_val)
    az.plot_posterior({'$\\theta$':beta.rvs(5, 11, size = 1000)})
    az.summary(trace)
    plt.show()

# The LOSS function

def loss_quadratic():

    grid = np.linspace(0, 1, 200)
    beta_pos = trace['beta']
    lossf_a = [np.mean(abs(i - beta_pos)) for i in grid]
    lossf_b = [np.mean((i - beta_pos)**2) for i in grid]

    for lossf, c in zip([lossf_a, lossf_b], ['CO', 'C1']):
        mini = np.argmin(lossf, c)
        plt.plot(grid, lossf, c)
        plt.plot(grid[mini], lossf[mini], 'o', color = c)
        plt.annotate('{:.2f}'.format(grid[mini]),
                                    (grid[mini], lossf[mini] + 0.03), color = c)
        plt.yticks([])
        plt.xlabel(r'$\hat \theta$')
