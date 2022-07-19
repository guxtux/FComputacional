#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 16:17:25 2020

@author: gustavo
"""

import math

def error_relativo(exacto, aproximado):
    return math.fabs(math.sin(exacto)- aproximado)/math.sin(exacto)*100

x = float(input('Teclea el valor a evaluar: '))

j=0
n = 10
suma = x
term =  x

print('x \t exacta \t   suma \t  error')
for i in range(2, n):
    j += 1
    term = (-term *x*x)/((2*i-1)*(2*i-2))
    suma  = suma + term
    print('{0:} \t {1:} \t {2:1.10f} \t {3:1.10f} \t {4:1.5e}'.format(j, x, math.sin(x), suma, error_relativo(x, suma)))
    