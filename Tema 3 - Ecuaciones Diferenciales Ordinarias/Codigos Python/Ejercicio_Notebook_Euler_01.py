#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 09:18:57 2022

@author: gustavo
"""

from metodosDirectos import euler
import numpy as np
from scipy import special
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['text.usetex'] = True

def F(x, y):
    f = np.zeros(1)
    f[0] = 1 - x * y[0]
    
    return f

def sol_exacta(x):
    return 0.5 * np.exp(-x**2/2) * (2 + np.sqrt(2 * np.pi) * special.erfi(x/np.sqrt(2)))
    # return ((1/2) * np.sqrt(2) * np.sqrt(np.pi)* special.erfi((1/2) * np.sqrt(2) * x) - 1/2 * np.sqrt(2) * np.sqrt(np.pi)* special.erfi((1/2) * np.sqrt(2)) + np.exp(1/2)) * np.exp(-1/2*x**2)

x = 0.0
xAlto = 5
y = np.array([1.])
h1 = 0.5
h2 = 0.01
x1 = np.linspace(0, 5)

X1, Y1 = euler(F, x, y, xAlto, h1)
X2, Y2 = euler(F, x, y, xAlto, h2)

plt.plot(X1, Y1[:,0], 'b', label=r'Gráfica con $h_1$ =' + str(h1))
plt.plot(X2, Y2[:,0], 'r', label=r'Gráfica con $h_2$ =' + str(h2))
plt.plot(x1, sol_exacta(x1), 'k--', label='Solución exacta')
plt.title('Solución a la EDO1 con el método de Euler')
plt.xlabel('x')
plt.ylabel('f (x)')
plt.legend(loc='best')
plt.xlim([0, 5])
plt.savefig('Ejercicio_Notebook_Euler_01.png', format='png')

plt.show()