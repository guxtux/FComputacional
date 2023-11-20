#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 13:47:43 2022

@author: gustavo
"""

from moduloMatrices import LUdescomp5, LUsoluc5
import numpy as np

def ecuaciones(x, h, m):
    h4 = h**4
    d = np.ones(m + 1) * 6.0
    e = np.ones(m) * (-4.0)
    f = np.ones(m-1)
    b = np.zeros(m+1)
    d[0] = 1.0
    d[1] = 7.0
    e[0] = 0.0
    f[0] = 0.0
    d[m-1] = 7.0
    d[m] = 3.0
    b[m] = 0.5 * h**3
    return d, e, f, b

xInicio = 0.0
xAlto = 0.5
m = 20
h = (xAlto - xInicio)/m
x = np.arange(xInicio,xAlto + h, h)
d, e, f, b = ecuaciones(x, h, m)

d, e, f = LUdescomp5(d, e, f)
y = LUsoluc5(d, e, f, b)

print('\n        x              y')
print('{0:14.5e} {1:14.5e}'.format(x[m-1], y[m-1]))
print('{0:14.5e} {1:14.5e}'.format(x[m], y[m]))