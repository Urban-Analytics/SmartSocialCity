'''
Name of class: main.py
Author: Sedar Olmez
Institute: Leeds Institute for Data Analytics
Date: 09/02/2019

Class description: This class is a sandbox for executing short methods developed
from the material in the pymc3 https://docs.pymc.io/ documentation and Bayesian
Analysis with Python book.
'''
import probability_functions as pf
import numpy as np
import pandas as pd

print(pf.probability_distribution_scipy(3))

mu_params = [-1, 0, 1]
sd_params = [0.5, 1, 1.5]
x = np.linspace(-7, 7, 200)
_, ax = plt.subplots(len(mu_params), len(sd_params), sharex = True,
                    sharey = True, figsize = (9, 7), constrained_layout = True)
for i in range(3):
    for j in range(3):
        mu = mu_params=[i]
        sd = sd_params[j]
        y = norm(mu, sd).pdf(x)
        ax[i, j].plot(x, y)
        ax[i, j].plot([], label = "u = {:3.2f}\no = {:3.2f}".format(mu, sd), alpha = 0)
        ax[i, j].legend(loc = 1)
ax[2, 1].set_xlabel('x')
ax[1, 0].set_ylabel('p(x)', rotation = 0, labelpad = 20)
ax[1, 0].set_yticks([])
