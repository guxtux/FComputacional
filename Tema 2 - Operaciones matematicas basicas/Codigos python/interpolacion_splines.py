# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 17:47:07 2020

@author: gusto
"""

from numpy import linspace
from scipy.interpolate import splrep, splev
import matplotlib.pyplot as plt

x = linspace(-1, 1, 100)
y = 1./(1 + 25 * x**2)

def trazador_cub(n):
    xi = linspace(-1, 1, n)
    yi = 1./(1 + 25 * xi**2)
    tck = splrep(xi, yi)
    return tck

tck = trazador_cub(8)
ys_8_ = splev(x, tck)

tck = trazador_cub(12)
ys_12_ = splev(x, tck)

plt.plot(x, y, label='f(x)')
plt.plot(x, ys_8_,'+g-', label='n=8')
plt.plot(x, ys_12_,'+r-',label ='n=12')
plt.legend(loc='best')
plt.title('Interpolación con splines cúbicos')
plt.ylim(-0.2, 1.2)
plt.axhline(y=0, ls='dashed', lw=0.7, color='k')
plt.show()