# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 14:20:47 2022

@author: gusto
"""

from scipy.stats import binom
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['text.usetex'] = True

n = 100
p = 0.4

r_valores = list(range(n+1))

dist = [binom.pmf(r, n, p) for r in r_valores]

plt.bar(r_valores, dist)
plt.title('Distribución binomial')
plt.savefig('plot_distribucion_01_binomial.eps', format='eps')
plt.savefig('plot_distribucion_01_binomial.png', format='png')
plt.show()