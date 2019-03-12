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
import data as dt
import coin_model as cm
from matplotlib import pyplot as plt
import pymc3 as pm
import nuclear_magnetic_resonance as nmr
import arviz as az
import numpy as np
from scipy import stats

data_cO2 = dt.csv_converter(r'/Users/solmez/SmartSocialCity/Probabilistic Programming/Experiments_with_PyMC3/mauna_C02.csv')

print(pf.probability_distribution_scipy(3))



#pf.probability_distribution_3by3_graphs()


#plt.plot(data_cO2[:, 0], data_cO2[:, 1])
#plt.xlabel('$year$', fontsize=16)
#plt.ylabel('$CO_2 (ppmv)$', fontsize=16)
#plt.savefig('B00001_01_02.png', dpi=300, figsize=(5.5, 5.5))
#cm.coin_flip()
#pf.beta_distribution_priori()
#pf.posterior_plot()
##cm.coin_flip_pymc3(123)
#pf.loss_quadratic()
#pf.asymmetric_loss_function()
nmr.NMR()
