# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 20:06:43 2013

@author: IIFCES
"""

import math as math

x=[0.1,1,10,100,1000]


def exponencial(x):
    diferencia = 0.
    cota = 1e-8
    calculada = 1.
    n=1
    while cota < math.fabs(calculada-math.exp(-x)):
        calculada = calculada + math.pow(-1.,n)*math.pow(x,n)/math.factorial(n)
        print n, calculada, math.exp(-x), math.fabs(calculada-math.exp(-x))
        n=n+1
    return n, x, math.exp(-x), calculada, diferencia 
    
for i in x:
    print exponencial(i)