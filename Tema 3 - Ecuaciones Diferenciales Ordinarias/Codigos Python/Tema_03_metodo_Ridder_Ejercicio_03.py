#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 13:19:31 2022

@author: gustavo
"""
from scipy.optimize import ridder
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['text.usetex'] = True

def f(x):
    return (x**2 - 1)
    
raiz1 = ridder(f, 0., 2.)
raiz2 = ridder(f, -2., 0.)

print('La raíz x1 es: {0:}'.format(raiz1))
print('\nLa raíz x2 es: {0:}'.format(raiz1))

x = np.linspace(-2., 2.)

# %% Rutina de graficación

plt.plot(x, f(x))
plt.plot(raiz1, 0, 'ro', label='Raíz $x_1$ = {0:1.1f}'.format(raiz1))
plt.plot(raiz2, 0, 'ro', label='Raíz $x_2$ = {0:1.1f}'.format(raiz2))
plt.title(r'La función $f (x)$ con sus raíces calculadas por la función $\texttt{ridder}$')
plt.xlabel(r'$x$', fontsize=12)
plt.ylabel(r'$f (x)$', fontsize=12)
plt.text(-1, 0.5, '$x_1 = $ {0:1.1f}'.format(raiz2), fontsize=12)
plt.text(0.5, 0.5, '$x_2 = $ {0:1.1f}'.format(raiz1), fontsize=12)
plt.axhline(y=0, lw=0.7, ls='dashed', color='k')
plt.savefig('plot_Metodo_Ridder_Ejercicio_03_01.png', format='png')
plt.savefig('plot_Metodo_Ridder_Ejercicio_03_01.eps', format='eps')
plt.show()