#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 13:44:29 2020

@author: gustavo
"""

from math import pi, e, exp, sqrt, factorial
from Modulo_Examen_01 import error_abs, error_relativo

incisos = [['a', pi, 22./7.], ['b', pi, 3.1416], ['c', e, 2.718], 
           ['d', sqrt(2), 1.141], ['e', exp(10), 22000], ['f', pow(10, pi), 1400],
           ['e', factorial(8), 39900], ['f', factorial(9), sqrt(18*pi)*pow((9./e),9)]]


print('Inciso \t \t E_absoluto \t \t E_relativo')
print('-'*55)
for i in range(8):
    print('Inciso {0:s} \t {1:1.8e} \t {2:1.8e}'.format(incisos[i][0], error_abs(incisos[i][1], incisos[i][2]), 
              error_relativo(incisos[i][1], incisos[i][2])))