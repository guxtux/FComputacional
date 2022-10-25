#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: gustavo
"""

from metodosDirectos import euler
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['text.usetex'] = True

def F(x, y):
    f = np.zeros(2)
    f[0] = y[1]
    f[1] = - 2 * g * y[0]
    
    return f

def F_friccion(x, y):
    f = np.zeros(2)
    f[0] = y[1]
    f[1] = - 2 * g * y[0] - beta * y[1]
    
    return f

def etiquetas():
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Desplazamiento [cm]')
    plt.xlim([0, 10])
    plt.axhline(y=0, ls='dashed', lw=0.7, color='k')
    
g = 9.81
x = 0.0
xAlto = 10.
y = np.array([2., 0.])
h = 0.001

beta = 0.8

X, Y = euler(F, x, y, xAlto, h)

X_friccion, Y_friccion = euler(F_friccion, x, y, xAlto, h)

plot1 = plt.figure(1)
plt.plot(X, Y[:,0])
plt.title('Nivel del agua en el tubo - Método de Euler')
etiquetas()

plot2 = plt.figure(2)
plt.plot(X_friccion, Y_friccion[:,0])
plt.title('Nivel del agua en el tubo con fricción - Método de Euler')
etiquetas()

plt.show()
