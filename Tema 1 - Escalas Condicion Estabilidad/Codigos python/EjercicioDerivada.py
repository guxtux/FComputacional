# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 22:05:44 2013

@author: IIFCES
"""

import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
mpl.rcParams['text.usetex'] = True

def funcion(h):
    derivada = (np.sin(2 * np.pi * (0.45 + h)) - np.sin(2 * np.pi * 0.45))/h
    return derivada

def etiquetas():
    plt.xlabel('Valor de h = $10^{-n}$')
    plt.ylabel('Error relativo')
    plt.title('Comportamiento del error al calcular la derivada de $\sin (x)$')

aproximacion = []
errores = []
i = []

exacta = -5.97566
h = 1e-1

print('h \t \t Aprox. derivada \t error relativo')
print('-'*40)

while h > 1e-16:
    aproximacion.append(funcion(h))
    errores.append(np.abs((exacta - aproximacion[-1])/exacta))
    i.append(h)    
    h = h/10
    print('{0:1.1e} \t {1:1.6f} \t {2:1.6e}'.format(i[-1], aproximacion[-1], errores[-1]))

plot1 = plt.figure(1)
plt.plot(errores, '+b')
plt.plot(errores, color='r', lw=0.7, ls='dashed')
etiquetas()

plot2 = plt.figure(2)
plt.yscale('log')
plt.plot(i)
plt.plot(errores, '+b')
plt.plot(errores, color='r', lw=0.7, ls='dashed')
etiquetas()

plt.show()