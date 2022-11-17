#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: gustavo
"""
from moduloMatrices import householder, calculaP, eigenvalores3, potenciaInversa3
import numpy as np

N = 3
a = np.array([[ 11.0, 2.0,  3.0,  1.0,  4.0],
              [  2.0, 9.0,  3.0,  5.0,  2.0],
              [  3.0, 3.0, 15.0,  4.0,  3.0],
              [  1.0, 5.0,  4.0, 12.0,  4.0],
              [  4.0, 2.0,  3.0,  4.0, 17.0]])

xx = np.zeros((len(a), N))

d, c = householder(a)

p = calculaP(a)

lambdas = eigenvalores3(d, c, N)

for i in range(N):
    s = lambdas[i] * 1.0000001
    lam, x = potenciaInversa3(d, c, s)
    xx[:,i] = x

xx = np.dot(p,xx)

print('Eigenvalores \n {0:}'.format(lambdas))
print('\nEigenvectores: \n{0:}'.format(xx))
