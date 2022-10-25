#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 10:40:46 2022

@author: gustavo
"""

from scipy.integrate import odeint
from numpy import zeros, array, linspace, pi
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['text.usetex'] = True

def F(y, t, zeta, w0):
    F = zeros((2), dtype='float64')
    F[0] = y[1]
    F[1] = -2 * zeta * w0 * y[1] - w0**2 * y[0]
    return F    

y0 =array([1.0, 0.0])

t = linspace(0, 7, 500)
w0 = 2 * pi * 1.0

y1 = odeint(F, y0, t, args=(0.0, w0))
y2 = odeint(F, y0, t, args=(0.2, w0))
y3 = odeint(F, y0, t, args=(1.0, w0))
y4 = odeint(F, y0, t, args=(5.0, w0))

plt.axis([0, 7, -1.05, 1.05])
plt.plot(t, y1[:,0], 'k', label="no amortiguado")
plt.plot(t, y2[:,0], 'r', label="subamortiguado")
plt.plot(t, y3[:,0], 'b', label="amortiguado critico")
plt.plot(t, y4[:,0], 'g', label="sobreamortiguado")
plt.title('Gráfica con los diferentes valores del factor de amortiguamiento')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.legend()
plt.savefig('plot_Ejercicio_odeint_02_Pendulo_Casos.eps', format='eps')
# plt.savefig('plot_Ejercicio_odeint_02_Pendulo_Casos.png', format='png')
plt.show()