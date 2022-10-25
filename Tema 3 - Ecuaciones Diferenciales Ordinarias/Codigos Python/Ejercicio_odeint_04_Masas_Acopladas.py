#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 13:02:12 2022

@author: gustavo
"""
from numpy import zeros, array, linspace
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['text.usetex'] = True

def F(y, t) :
    F = zeros(6)
    F[0] = y[3]
    F[1] = y[4]
    F[2] = y[5]
    F[3] = (-0.1 * y[3]- y[0] + 0.1 * y[4] + y[1] + 1.)
    F[4] = (0.1 * y[3] + y[0] - 0.1 * y[4] - 2. * y[1] + y[2])
    F[5] = (y[1] - 0.1 * y[5] - 2. * y[2])

    return F

t = linspace(0, 61, 200)
y0 = array([0., 0., 0., 0., 0., 0.])

sol = odeint(F, y0, t)

plt.plot(t, sol[:,0], label = r"$M_1$")
plt.plot(t, sol[:,1], label = r"$M_2$")
plt.plot(t, sol[:,2], label = r"$M_3$")
plt.title("Solución al sistema de tres masas acopladas")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.axis([0, 60, -0.5, 6])
plt.axhline(y=0, lw=0.75, ls='dashed', color='k')
plt.legend(loc='upper right')
plt.savefig('plot_Ejercicio_odeint_04_Masas_Acopladas.eps', format='eps')
plt.savefig('plot_Ejercicio_odeint_04_Masas_Acopladas.png', format='png')
plt.show()