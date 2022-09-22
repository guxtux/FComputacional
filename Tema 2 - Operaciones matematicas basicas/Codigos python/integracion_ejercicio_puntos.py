# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 07:24:58 2022

@author: gusto
"""

from moduloIntegracion import simpson38puntos, simpson18puntos
from scipy import interpolate
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['text.usetex'] = True

def etiquetas():
    plt.xlabel(r'$x$')
    plt.ylabel(r'$f(x)$')

x = [0, 0.5, 1.0, 1.5, 2.0, 2.5]
fx = [1.5000, 2.0000, 2.0000, 1.6364, 1.25000, 0.9565]

print(fx[:4])
print(fx[3:])

integral1 = simpson38puntos(fx[:4], 4, 0.5)
integral2 = simpson18puntos(fx[3:], fx[-3], 3, 0.5)

print('Valor de la integral por la  regla de 3/8 de Simpson = {0:1.6f}'.format(integral1))
print('\nValor de la integral por la  regla de 1/8 de Simpson = {0:1.6f}'.format(integral2))

print('\nValor de la integral = {0:1.6f}'.format(integral1 + integral2))

x0 = np.linspace(0.01, 2.5, 100)

f2 = interpolate.interp1d(x, fx, kind="quadratic")
y2 = f2(x0)


plot1 = plt.figure(1)
plt.plot(x, fx, '+b')
plt.title('Datos de la tabla')
etiquetas()

plot2 = plt.figure(2)
plt.plot(x, fx, '+b')
plt.plot(x0, y2, 'r', lw=0.7)
plt.title('Integral a partir de reglas de Simpson')
plt.fill_between(x[:4], 0, fx[:4], color='g', label='Simpson 3/8')
plt.fill_between(x[3:], 0, fx[3:], color='b', label='Simpson 1/8')
for i in range(0, 5, 1):
    plt.axvline(x[i], color='w', lw=0.7)
plt.legend(loc='best')
plt.axis([0, 2.5, 0, 2.2])
etiquetas()

plt.show()