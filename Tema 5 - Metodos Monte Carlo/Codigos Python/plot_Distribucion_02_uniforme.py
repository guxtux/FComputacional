# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 15:36:50 2022

@author: gusto
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['text.usetex'] = True

s = np.random.uniform(-1, 0, 1000)

count, bins, ignored = plt.hist(s, 15, density=True)
plt.plot(bins, np.ones_like(bins), linewidth=2, color='r')
plt.title('Distribución uniforme')
plt.savefig('plot_distribucion_02_uniforme.eps', format='eps')
plt.savefig('plot_distribucion_02_uniforme.png', format='png')

plt.show()