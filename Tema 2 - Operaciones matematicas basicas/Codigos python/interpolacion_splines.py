# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 17:47:07 2020

@author: gusto
"""

from numpy import linspace
from scipy.interpolate import splrep, splev
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['text.usetex'] = True

def funcionInicial(x):
    valor = 1./(1 + 25 * x**2)
    return valor

def trazador_cub(n):
    xi = linspace(-1, 1, n)
    tck = splrep(xi, funcionInicial(xi))
    return tck


x = linspace(-1, 1, 100)


tck1 = trazador_cub()
ys8 = splev(x, tck1)

tck2 = trazador_cub()
ys12 = splev(x, tck2)

plt.plot(x, funcionInicial(x), label='f(x)')
plt.plot(x, ys8,'+g-', lw=0.7, label='n=8')
plt.plot(x, ys12,'+r-', lw=0.7, label ='n=12')
plt.legend(loc='best')
plt.title('Interpolación con splines cúbicos')
plt.ylim(-0.2, 1.2)
plt.axhline(y=0, ls='dashed', lw=0.7, color='k')
plt.show()