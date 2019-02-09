'''
Name of class: data.py
Author: Sedar Olmez
Institute: Leeds Institute for Data Analytics
Date: 09/02/2019

Class description: This class is a sandbox for executing short methods developed
from the material in the pymc3 https://docs.pymc.io/ documentation and Bayesian
Analysis with Python book.
'''
import numpy as np

def __init__():
    pass


def csv_converter(path):
    data = np.genfromtxt(path, delimiter=',')
    return data
