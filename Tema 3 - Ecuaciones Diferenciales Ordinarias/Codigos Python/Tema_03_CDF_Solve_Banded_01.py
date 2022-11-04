#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 18:03:01 2022

@author: gustavo
"""

from scipy.linalg import solve_banded
from numpy import array

ab = array([[0,  0, -1, -1, -1],
            [0,  2,  2,  2,  2],
            [5,  4,  3,  2,  1],
            [1,  1,  1,  1,  0]])

b = array([0, 1, 2, 2, 3])

x = solve_banded((1, 2), ab, b)

print(x)

ab2 = array([[0, -1, -1, -1, -1],
             [2, 2, 2, 2, 2],
             [-1, -1, -1, -1, 0]])

b2 = array([5., -5, 4, -5, 5])

x2 = solve_banded((1, 1), ab2, b2)
print('\nLa solución al problema con la matriz tridiagonal es:')
print(x2)

