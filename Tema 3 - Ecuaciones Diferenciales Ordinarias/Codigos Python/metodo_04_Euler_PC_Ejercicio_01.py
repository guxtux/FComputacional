#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 15:01:01 2022

@author: gustavo
"""

from metodosDirectos import eulerPC
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['text.usetex'] = True


def f(x, y, f):
    f[0] = y[1]
    f[1] = -y[0]
    return f

n = 2
x = 0.0
xAlto = 100.0
y = np.array([0., 1.])
h = 0.05

nt = int(xAlto/h + 0.5) + 1

y1 = np.zeros(nt+1)
y2 = np.zeros(nt+1)
it = np.zeros(nt+1)

y1[0] = y[0]
y2[0] = y[1]
iteracion = 1

while (x + h <= xAlto):
    eulerPC(x, h, y, n, f)
    x += h
    iteracion += 1
    y1[iteracion] = y[0]
    y2[iteracion] = y[1]
    it[iteracion] = iteracion

plot1 = plt.figure(1)
plt.plot(it[2:], y1[2:], 'r')
plt.title('Solución a la EDO')
plt.xlim([0, 2000])
plt.axhline(y=0, ls='dashed', lw=0.7, color='k')
plt.xlabel('x')
plt.ylabel('y(x)')
# plt.savefig('plot_eulerPC_ejercicio_01.eps', format='eps')

plot2 = plt.figure(2)
plt.plot(y1[2:], y2[2:], 'r')
plt.title('Espacio fase del problema')
plt.xlabel('y1')
plt.ylabel('y2')
# plt.savefig('plot_eulerPC_ejercicio_02.eps', format='eps')

plt.show()