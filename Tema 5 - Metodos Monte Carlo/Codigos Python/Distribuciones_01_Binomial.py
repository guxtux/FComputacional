#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: gustavo
"""

from scipy.stats import binom
import matplotlib.pyplot as plt

# Marca error de que no encuentra los fonts

# import matplotlib as mpl

# mpl.rcParams['text.usetex'] = True

n = 100
p = 0.3

r_valores = list(range(n+1))

dist = [binom.pmf(r, n, p) for r in r_valores]

plt.bar(r_valores, dist)
plt.savefig('plot_distribucion_01_binomial.eps', format='eps')
# plt.savefig('plot_distribucion_01_binomial.png', format='png')
plt.show()