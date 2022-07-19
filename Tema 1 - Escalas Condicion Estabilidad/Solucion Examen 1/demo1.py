# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 15:30:13 2013

@author: IIFCES
"""


from math import *

x= 0.1
n = 1
calculada= 1.

for i in range(11):
    calculada = calculada + (-1.)**n*x**n/factorial(n)
    print n, (-1.)**n*x**n/factorial(n), calculada
    n=n+1