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
    f[0] = y[1]
    f[1] = g * (1 - a * y[0]**3)
    return f

g = 9.81
a = 16
x = 0.0
xAlto = 10.0
y = np.array([0., 0.1])
h = 0.01

X, Y = integraorden4(f, x, y, xAlto, h)

plt.plot(X, Y[:,0])
plt.title('Solución al ejercicio del flotador')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [m]')
plt.xlim([0,10])
plt.show()