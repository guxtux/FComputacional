# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 13:10:55 2022

@author: gusto
"""

from moduloMatrices import jacobi
from numpy import array, sqrt

a = array([[ 3, -2, 0, 0], \
           [-2, 5, -3, 0], \
            [ 0, -3, 7, -4], \
           [ 0, 0, -4, 9]])*1.0
    
lam, x = jacobi(a)

print('Eigenvalores del sistema: ')
print(lam)
print()
print("Frecuencias angulares (unidades de 1/sqrt(LC)):")
print(sqrt(lam))