#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 16:17:25 2020

@author: gustavo
"""

import math

def error_relativo(exacto, aproximado):
    return math.fabs(math.exp(exacto)- aproximado)/math.exp(exacto)*100

x = float(input('Teclea el valor a evaluar: '))

n = 50
suma = x
term =  x

print('x \t exacta \t   suma \t  error')
for i in range(2, n):
    term = (term * x)/(i * (i - 1))
    suma  = suma + term
    print('{0:} \t {1:} \t {2:} \t {3:1.11e}'.format(x, math.exp(x), suma+1, error_relativo(x, suma+1)))
    