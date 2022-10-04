#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 15:10:31 2022

@author: gustavo
"""

from metodosDirectos import euler
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['text.usetex'] = True


def f(x, y):
    f = np.zeros(2)
    f[0] = y[1]
    f[1] = -y[0]
    return f

x = 0.0
xAlto = 100.0
y = np.array([0., 1.])
h = 0.05

X, Y = euler(f, x, y, xAlto, h)


plot1 = plt.figure(1)
plt.plot(X, Y[:,0])
plt.title('Solución numérica del ejercicio')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim([0, 100])
plt.axhline(y=0, ls='dashed', lw=0.7, color='k')
# plt.savefig('plot_euler_ejercicio_04.eps', format='eps')

plot2 = plt.figure(2)
plt.plot(Y[:,0], Y[:,1])
plt.title('Espacio fase del problema')
# plt.savefig('plot_euler_ejercicio_05.eps', format='eps')
plt.show()