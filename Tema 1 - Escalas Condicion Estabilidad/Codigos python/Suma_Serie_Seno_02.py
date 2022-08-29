#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 17:38:24 2020

@author: gustavo
"""

import math

def error_relativo(exacto, aproximado):
    return math.fabs(math.sin(exacto)- aproximado)/math.sin(exacto)*100

a = float(input('Teclea el valor a evaluar: '))
x = math.radians(a)

#x = [-2, -1.5, -1, -0.5, 0.5, 1, 1.5, 2]



tolerancia = 1e-8
error = 1.
suma = x
term =  x
i = 2



print('x \t aproximacion \t  error')

while error > tolerancia:
    term = (-term * i * i)/((2 * i - 1) * (2 * i - 2))
    suma  = suma + term
    error = error_relativo(x, suma)
    print('{0:} \t {1:1.10f} \t {2:1.5e}'.format(i, suma, error))
    i = i + 1
    