# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 19:51:36 2020

@author: gusto
"""

import numpy as np
n = 3
x_0_ = np.array([1.5, 2.5, 3.5])
x = np.array([1., 2., 3., 4.])
f = np.array([0.671, 0.620, 0.567, 0.512])

for k in x_0_:
    yres = 0
    for i in range(0, n + 1):
        z = 1.0
        for j in range(0, n + 1):
            if i != j:
                z = z * (k - x[j])/(x[i] - x[j])
        yres = yres + z*f[i]
    
    print ('El polinomio evaluado en P(',k,') =',  yres)