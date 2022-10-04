#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 20:05:14 2022

@author: gustavo
"""

from metodosDirectos import integraorden4
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['text.usetex'] = True

def f(x, y):
    f = np.zeros(2)
    f[0] = y[1]
    f[1] = -0.1 * y[1] - x
    return f

x = 0.0
xAlto = 2.0
y = np.array([0., 1.])
h = 0.2

X, Y = integraorden4(f, x, y, xAlto, h)
s_Exacta = 100. * X - 5. * X**2 + 990. *(np.exp(-0.1 * X) - 1.)

plt.plot(X, Y[:,0], '+r')
plt.plot(X, s_Exacta, '-b')
plt.title('Comparación entre la solución aproximada y la exacta')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim([0, 2])
plt.legend(('Numérica', 'Exacta'), loc=0)
# plt.savefig('plot_rk4_ejercicio_01.eps', format='eps')
plt.show()