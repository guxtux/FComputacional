#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: gustavo
"""

import numpy as np

def f(x):
    return 2 + 3*x

def MCintvec(f, a, b, n):
    x = np.random.uniform(a, b, n)
    s = np.sum(f(x))
    I = (float(b-a)/n) * s
    
    return I

integral = MCintvec(f, 1, 2, 100)

print('Valor de la integral: {0:}'.format(integral))
print('Error absoluto: {0:1.5e}'.format(6.5 - integral))