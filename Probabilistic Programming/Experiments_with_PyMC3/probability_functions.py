'''
Name of class: probability_functions.py
Author: Sedar Olmez
Institute: Leeds Institute for Data Analytics
Date: 09/02/2019

Class description: This class is a sandbox for executing short methods developed
from the material in the pymc3 https://docs.pymc.io/ documentation and Bayesian
Analysis with Python book.
'''
from scipy.stats import norm

def __init__():
    pass

def probability_distribution_scipy(random_variate_index):
    X = norm(0, 1)
    x = X.rvs(random_variate_index)
    return x
