#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: gustavo
"""

import numpy as np

def f(x):
    return 2 + 3*x

def MCint3(f, a, b, n, N=100):
    s = 0
    Ivalores = []
    kvalores = []
    
    for k in range(1, n+1):
        x = np.random.uniform(a, b)
        s += f(x)
        if k % N == 0:
            I = (float(b-a)/k) * s
            Ivalores.append(I)
            kvalores.append(k)
    
    return kvalores, Ivalores

k, integral = MCint3(f, 1, 2, 1000000, N=10000)

error = 6.5 - integral[-1]

print('Valor de la integral: {0:}'.format(integral[-1]))
print('Error absoluto: {0:1.5e}'.format(error))