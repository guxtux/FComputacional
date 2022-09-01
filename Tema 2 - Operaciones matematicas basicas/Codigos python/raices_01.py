#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 13:27:58 2022

@author: gustavo
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize

mpl.rcParams['text.usetex'] = True


def buscaraiz(f, a, b, dx):
    x1 = a; f1 = f(a)
    x2 = a + dx; f2 = f(x2)
    while f1 * f2 > 0.0:
        if x1 >= b: return None
        x1 = x2; f1 = f2
        x2 = x1 + dx; f2 = f(x2)
    else:
        return x1, x2


coeficientes = [1, -7, 2, 1]
x = np.linspace(-5, 4)

p = np.polynomial.polynomial.Polynomial(coeficientes)
y = np.polynomial.polynomial.polyval(x, coeficientes)

a = -5
b = 4
raices = []
a1 = range(1, 10)

x1, x2 = buscaraiz(p, -5, -4 , 0.1)
raiz = optimize.bisect(p, x1, x2)
print(raiz)
raices.append(raiz)

x1, x2 = buscaraiz(p, -0.5, 0.5, 0.1)
raiz = optimize.bisect(p, x1, x2)
print(raiz)
raices.append(raiz)

x1, x2 = buscaraiz(p, 1.5, 2.5, 0.1)
raiz = optimize.bisect(p, x1, x2)
print(raiz)
raices.append(raiz)

print(raices)

# for i in a1:
#     print(i)

# for i in a1:
#     a = i
#     x1, x2 = buscaraiz(p, a, a + 1, 0.1)
#     raiz = optimize.bisect(p, x1, x2)
#     print(raiz)
#     raices.append(raiz)

    
# print(raices)

#  , b = buscaraiz(p, -5, 4, 0.1)
# print(a, b)

# raiz = optimize.bisect(p, -4, -2)
# print(raiz)
ydatos = [0, 0, 0]

plt.plot(x, y, label = 'Función')
plt.plot(raices, ydatos, 'om', label='Raíces')
plt.title('Raíces de f(x)')
plt.xlabel('$x$')
plt.ylabel('$f (x)$')
plt.axhline(y=0, ls='dashed', lw=0.7, color='k')
plt.legend(loc='best')
plt.show()