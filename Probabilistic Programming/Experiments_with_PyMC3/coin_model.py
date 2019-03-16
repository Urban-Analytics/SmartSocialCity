'''
Name of class: coin_model.py
Author: Sedar Olmez
Institute: Leeds Institute for Data Analytics
Date: 09/02/2019

Class description: This class is a sandbox for executing short methods developed
from the material in the pymc3 https://docs.pymc.io/ documentation and Bayesian
Analysis with Python book.
'''
class Coin:

    import numpy as np
    from matplotlib import pyplot as plt
    from scipy.stats import norm
    from scipy.stats import binom
    from scipy import stats
    import pymc3 as pm
    import arviz as az

    n_params = [1, 2, 4]
    p_params = [0.25, 0.5, 0.75]
    seed = 0
    x = np.arange(0, max(n_params) + 1)
    f, ax = plt.subplots(len(n_params), len(p_params), sharex = True,
                        sharey = True, figsize=(8, 7), constrained_layout = True)


    def __init__(self, seed, n_params, p_params):
        self.seed = seed
        self.n_params = n_params
        self.p_params = p_params


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


    def coin_flip_pymc3(seed):
        np.random.seed(seed)
        trials = 4
        theta_real = 0.35
        data = stats.bernoulli.rvs(p = theta_real, size = trials)

        with pm.Model() as our_first_model:
            beta = pm.Beta('O', alpha = 1., beta = 1.) # <--- Prior
            y = pm.Bernoulli('y', p = beta, observed = data) # <--- likelihood
            trace = pm.sample(1000, random_seed = 123)
            az.plot_trace(trace) # <---- plotting the results
            az.plot_posterior(trace) # <---- plotting the posterior graph
            print(az.summary(trace))
            plt.show()
