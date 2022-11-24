#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: gustavo
"""

import numpy as np
import matplotlib.pyplot as plt

def curvaNormal(x, mu, sigma):
    valor = 1/(sigma * np.sqrt(2 * np.pi)) \
    * np.exp( - (bins - mu)**2 / (2 * sigma**2)) 
    
    return valor
    

mu, sigma = 0, 0.1 # media y desviación estándar
s = np.random.normal(mu, sigma, 1000)

count, bins, ignored = plt.hist(s, 30, density=True)
plt.plot(bins, curvaNormal(bins, mu, sigma), linewidth=2, color='r')
plt.savefig('plot_distribucion_03_gaussiana.eps', format='eps')
plt.show()