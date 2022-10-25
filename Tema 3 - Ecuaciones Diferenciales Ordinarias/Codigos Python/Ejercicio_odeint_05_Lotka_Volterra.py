#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 13:38:24 2022

@author: gustavo
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['text.usetex'] = True


def dXdt(X, t = 0):
    return np.array([ a * X[0] - b * X[0] * X[1], - c * X[1] + d * b * X[0] * X[1]])

a = 1.
b = 0.1
c = 1.5
d = 0.75

Xf0 = np.array([0., 0.])
Xf1 = np.array([ c/(d * b), a/b])
all(dXdt(Xf0) == np.zeros(2) ) and all(dXdt(Xf1) == np.zeros(2))

t = np.linspace(0, 15,  1000)
              
X0 = np.array([10, 5])         
            
X = odeint(dXdt, X0, t)

conejos, zorros = X.T

plot1 = plt.figure(1)
plt.plot(t, conejos, 'r-', label='Conejos')
plt.plot(t, zorros  , 'b-', label='Zorros')
plt.title('Evolución de la población de conejos y zorros')
plt.xlabel('Tiempo')
plt.ylabel('Población')
plt.xlim([0, 15])
plt.grid()
plt.legend(loc='best')

plt.show()

# %% Consideremos las condiciones de equilibrio, es decir, donde la tasa de crecimiento es cero:

Xf0 = np.array([0. , 0.])
Xf1 = np.array([ c/(d * b), a/b])

values  = np.linspace(0.3, 0.9, 5)                         

vcolors = plt.cm.autumn_r(np.linspace(0.3, 1., len(values)))  

plot2 = plt.figure(2)

for v, col in zip(values, vcolors):
    X0 = v * Xf1
    X = odeint(dXdt, X0, t)
    
    plt.plot(X[:,0], X[:,1], lw=3.5 * v, color=col, label='({0:1.1f} , {1:1.1f}'.format(X0[0], X0[1]))

ymax = plt.ylim(ymin = 0)[1]
xmax = plt.xlim(xmin = 0)[1]

nbpoints = 20

x = np.linspace(0, xmax, nbpoints)
y = np.linspace(0, ymax, nbpoints)

X1, Y1  = np.meshgrid(x, y)

DX1, DY1 = dXdt([X1, Y1])                      

M = (np.hypot(DX1, DY1))

M[ M == 0] = 1.                                 

DX1 /= M                                        
DY1 /= M

plt.title('Trayectorias y campo de dirección - Sistema Lotka-Volterra')

Q = plt.quiver(X1, Y1, DX1, DY1, M, pivot='mid', cmap=plt.cm.jet)

plt.xlabel('Población de conejos')
plt.ylabel('Población de zorros')
plt.legend()
plt.grid()
plt.xlim(0, xmax)
plt.ylim(0, ymax)
plt.show()
