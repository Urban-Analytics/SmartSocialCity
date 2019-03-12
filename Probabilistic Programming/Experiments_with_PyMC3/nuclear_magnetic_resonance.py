'''
Name of class: nuclear_magnetic_resonance.py
Author: Sedar Olmez
Institute: Leeds Institute for Data Analytics
Date: 12/03/2019

Class description: This class is a sandbox for executing short methods developed
from the material in the pymc3 https://docs.pymc.io/ documentation and Bayesian
Analysis with Python book.
'''
import arviz as az
import numpy as np

def __init__():
    pass

def NMR():
    data = np.loadtxt('../data/chemical_shifts.csv')
    az.plot_kde(data, rug=True)
    plt.yticks([0], alpha = 0)
