#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 19:05:57 2022

@author: gustavo
"""

from metodosDirectos import integraorden4
import numpy as np

def f(x, y):
    f = np.zeros(1)
    f[0] = 3 * y[0] - 4 * np.exp(-x)
    return f

x = 0.0
xAlto = 10.0
y = np.array([1.])
h = 0.1

X, Y = integraorden4(f, x, y, xAlto, h)
s_Exacta = np.exp(-X)