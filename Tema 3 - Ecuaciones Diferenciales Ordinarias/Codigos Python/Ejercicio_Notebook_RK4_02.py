#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: gustavo
"""

from metodosDirectos import integraorden4
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['text.usetex'] = True

def f(x, y):
    f = np.zeros(2)
    
    if x < 2:
        P = 10 * x
    else:
        P = 20
    
    f[0] = y[1]
    f[1] = (P/m) - (k/m) * y[0]
    return f

m = 0.25
k = 75
x = 0.0
xAlto = 5.0
y = np.array([0., 0.])
h = 0.01

X, Y = integraorden4(f, x, y, xAlto, h)

plt.plot(X, Y[:,0])
plt.title('Solución al ejercicio del sistema masa-resorte')
plt.xlabel('Tiempo [s]')
plt.ylabel('Desplazamiento [m]')
plt.xlim([0, 5])
plt.show()