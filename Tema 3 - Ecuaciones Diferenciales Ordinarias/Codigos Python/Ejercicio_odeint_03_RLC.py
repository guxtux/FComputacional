#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 11:04:49 2022

@author: gustavo
"""

from numpy import zeros, array, linspace
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['text.usetex'] = True


def F(y, t, R, L) :
    C = 0.001
    E = 1.0
    
    F = zeros(2)
    F[0] = y[1]
    F[1] = -(R/L) * y[1] - (1.0/(L * C)) * y[0] + E/L
    
    return F

t = linspace(0.0, 5.0, 100)
y0 = array([0., 0.])
h = 0.01

L = 200.0
R = [0., 50, 100, 300]

for r in R:
    sol = odeint(F, y0, t, args=(r, L))
    plt.plot(t,sol[:,1], label='R = ' + str(r) + ' $\Omega$')

plt.axhline(y=0, lw=0.75, ls='dashed', color='k')
plt.legend(loc='best')
plt.title(r'Solución de la EDO para distintos valores de $R$')
plt.xlim([0, 5])
plt.savefig('plot_Ejercicio_odeint_03_Circuito_RLC.eps', format='eps')
# plt.savefig('plot_Ejercicio_odeint_03_Circuito_RLC.png', format='png')
plt.show()