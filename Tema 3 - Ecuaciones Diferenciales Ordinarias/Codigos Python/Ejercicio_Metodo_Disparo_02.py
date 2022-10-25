#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 12:54:08 2022

@author: gustavo
"""

from metodosDirectos import integra_RKAdaptativo
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['text.usetex'] = True

def interpLineal(f, x1, x2):
    f1 = f(x1)
    f2 = f(x2)

    return x2 - f2 * (x2 - x1) / (f2 - f1)

def condIni(u):
    return np.array([0.0, 0.0, u])

def r(u):
    X, Y = integra_RKAdaptativo(F, xInicio, condIni(u), xAlto, h)
    y = Y[len(Y) - 1]
    r = y[0] - 2.0
    
    return r

def F(x, y):
    F = np.zeros(3)
    F[0] = y[1]
    F[1] = y[2]
    F[2] = 2.0 * y[2] + 6.0 * x * y[0]
    
    return F

def etiquetas(orden):
    plt.axhline(y=0, lw=0.7, color='k')
    plt.axhline(y=2, lw=0.7, ls='dashed', color='k')
    plt.xlabel(r'$x$')
    plt.xlim([0, 5])
    plt.legend(loc='best')
    handles, labels = plt.gca().get_legend_handles_labels()
    order = orden
    plt.legend([handles[idx] for idx in order],[labels[idx] for idx in order]) 

xInicio = 5.0
xAlto = 0.0
u1 = 1.0
u2 = 2.0
h = -0.1

# Primer intento de CI desconocida
u1 = 1.0
X1, Y1 = integra_RKAdaptativo(F, xInicio, condIni(u1), xAlto, h)

# Primer intento de CI desconocida
u2 = 2.0
X2, Y2 = integra_RKAdaptativo(F, xInicio, condIni(u2), xAlto, h)

# Valor de CI interpolada
u = interpLineal(r, u1, u2)
X3, Y3 = integra_RKAdaptativo(F, xInicio, condIni(u), xAlto, h)

plot1 = plt.figure(1)
plot1 = plt.figure(1)
plt.plot(X1, Y1[:,0], 'r', label=r'$u_1$ = {0:}'.format(u1))
plt.plot(X2, Y2[:,0], 'b', label=r'$u_2$ = {0:}'.format(u2))
plt.title('Solución con los valores de CI de prueba')
etiquetas([1, 0])
# plt.savefig('plot_Ejercicio_02_Metodo_Disparo_01.eps', format='eps')
# plt.savefig('plot_Ejercicio_02_Metodo_Disparo_01.png', format='png')

plot2 = plt.figure(2)
plt.plot(X3, Y3[:,0],'b.-', label='y')
plt.plot(X3, Y3[:,1], 'r.-', label='dy/dx')
plt.title(r'Solución con el valor $u$ interpolado')
etiquetas([1, 0])
# plt.savefig('plot_Ejercicio_02_Metodo_Disparo_02.eps', format='eps')
# plt.savefig('plot_Ejercicio_02_Metodo_Disparo_02.png', format='png')

plt.show()