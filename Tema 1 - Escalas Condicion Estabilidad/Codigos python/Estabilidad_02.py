#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 13:07:16 2022

@author: gustavo
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
mpl.rcParams['text.usetex'] = True

def funcion(n, x):
    return (x**n) * np.exp(x)

x = np.linspace(0, 1, 100)

n = [1, 2, 4, 8]

for i in n:
    plt.plot(x, funcion(i, x), label='n = {0:}'.format(i))

plt.title('Gráfica de la función')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend(loc='best')
plt.axis([0, 1, 0, 2.8])
plt.show()