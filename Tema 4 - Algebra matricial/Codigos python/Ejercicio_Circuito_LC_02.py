# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 12:14:51 2022

@author: gusto
"""

from moduloMatrices import jacobi
from numpy import array, sqrt

beta = array([1, 2, 3, 4])*1.0 # Diagonal terms of [B}
beta = sqrt(beta)

a = array([[ 2, -1, 0, 0], \
           [-1, 2, -1, 0], \
           [ 0, -1, 2, -1], \
           [ 0, 0, -1, 2]])*1.0

for i in range(4): # Form matrix [H} of std. problem
    for j in range(4):
        a[i,j] = a[i,j]/(beta[i]*beta[j])

lam, x = jacobi(a) # Solve by Jacobis method

print(lam)
print()
print("Circular frequencies (units of 1/sqrt(CL)):")
print(1.0/sqrt(lam))
