#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 20:49:02 2022

@author: gustavo
"""

from metodosDirectos import integraorden2
from prettytable import PrettyTable
import numpy as np

def f(x, y):
    f = np.zeros(1)
    f[0] = np.sin(y)
    return f

x = 0.0
xAlto = 0.5
y = np.array([1.])
h = 0.1

exactas = [1, 1.08635575, 1.17682011, 1.27081689, 1.36762622, 1.46640400]

tabla = PrettyTable()
tabla.field_names = ['x', 'Aproximación', 'Error']

X, Y = integraorden2(f, x, y, xAlto, h)

for i in range(len(X)):
    error = np.fabs(exactas[i] - Y[i])
    tabla.add_row(['%1.1f' % X[i],'%1.8f' % Y[i], '%1.6e' % error])

print(tabla)