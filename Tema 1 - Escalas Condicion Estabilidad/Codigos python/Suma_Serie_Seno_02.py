#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 17:38:24 2020

@author: gustavo
"""

import math

def error_relativo(exacto, aproximado):
    return math.fabs(math.sin(exacto)- aproximado)/math.sin(exacto)*100

#x = float(input('Teclea el valor a evaluar: '))


x = [-2, -1.5, -1, -0.5, 0.5, 1, 1.5, 2]



tolerancia = 1e-8
n = 10





print('x \t exacta \t   suma \t  error')
for j in x:
    suma = j
    term =  j
    for i in range(2, n):
        term = (-term *j*j)/((2*i-1)*(2*i-2))
        suma  = suma + term
    print('{0:} \t {1:1.10f} \t {2:1.10f} \t {3:1.5e}'.format(j, math.sin(j), suma, error_relativo(j, suma)))
    