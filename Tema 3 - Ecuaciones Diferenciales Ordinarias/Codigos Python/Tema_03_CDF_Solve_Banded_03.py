#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 18:23:51 2022

@author: gustavo
"""

from scipy.linalg import solve_banded
import numpy as np

def ecuaciones(x, h, m):
    d = np.ones(m) * 6.0
    e = np.ones(m) * (-4.0)
    f = np.ones(m)
    c = e.copy()
    g = f.copy()
    b = np.zeros(m)
    
    d[0] = 1.0
    d[1] = 7.0
    d[-1] = 3.0
    d[-2] = 7.0
    
    e[0] = 0.0
    e[1] = 0.0
    
    f[0] = 0.0
    f[1] = 0.0
    f[2] = 0.0
    
    c[0] = 0.0
    c[-1] = 0.0
    
    g[0] = 0.0
    g[-1] = 0.0
    g[-2] = 0.0
    
    b[-1] = 0.5 * h**3
    
    return f, e, d, c, g, b

xInicio = 0.0
xAlto = 0.5
m = 20
h = (xAlto - xInicio)/m
x = np.arange(xInicio,xAlto + h, h)

f, e, d, c, g, b = ecuaciones(x, h, m+1)

ab = np.array([f, e, d, c, g])


# %% Solución al problema matricial

solucion = solve_banded((2, 2), ab, b)

print('\n        x              y')
print('{0:14.5e} {1:14.5e}'.format(x[-2], solucion[-2]))
print('{0:14.5e} {1:14.5e}'.format(x[-1], solucion[-1]))
