#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: gustavo
"""

from metodosDirectos import integraorden4
import numpy as np
import matplotlib.pyplot as plt

def F(x, y):
    F = np.zeros(2)
    F[0] = y[1]
    F[1] = (((np.pi**2)/12.0)**2)*y[0]*((np.sin((np.pi)*x))**2) \
        -9.80665*(np.sin ((np.pi/12.0)*(np.cos(x*np.pi))))
    
    return F


x = 0.0
xAlto = 4.0
y = np.array([0.75, 0])
h = 0.1

X, Y = integraorden4(F, x, y, xAlto, h)

plt.plot(X, Y[:,0])
plt.title('Solución al ejercicio')
#plt.savefig('plot_rk4_ejercicio_02_02.eps', format='eps')

plt.show()