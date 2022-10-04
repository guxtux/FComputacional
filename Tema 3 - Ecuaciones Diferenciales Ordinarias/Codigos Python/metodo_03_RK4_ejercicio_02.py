#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 19:05:57 2022

@author: gustavo
"""

from metodosDirectos import integraorden4
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['text.usetex'] = True


def f(x, y):
    f = np.zeros(1)
    f[0] = 3 * y[0] - 4 * np.exp(-x)
    return f

def etiquetas():
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim([0, 10])

x = 0.0
xAlto = 10.0
y = np.array([1.])
h = 0.1

X, Y = integraorden4(f, x, y, xAlto, h)
s_Exacta = np.exp(-X)

plot1 = plt.figure(1)
plt.plot(X, Y[:,0], '+r')
plt.title('Solución numérica con RK4')
etiquetas()
#plt.savefig('plot_rk4_ejercicio_02_01.eps', format='eps')

plot2 = plt.figure(2)
plt.plot(X, s_Exacta, '-b')
plt.title('Solución exacta al ejercicio')
etiquetas()
#plt.savefig('plot_rk4_ejercicio_02_02.eps', format='eps')

plt.show()


