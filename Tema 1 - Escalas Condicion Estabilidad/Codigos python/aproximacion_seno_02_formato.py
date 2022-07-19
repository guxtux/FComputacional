# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 19:55:08 2020

@author: gusto
"""
from prettytable import PrettyTable
import math

def error_relativo(exacto, aproximado):
    return math.fabs(math.sin(exacto)- aproximado)/math.sin(exacto)*100

x = [-2, -1.5, -1, -0.5, 0.5, 1, 1.5, 2]

n = 10

t = PrettyTable(['x', 'exacta', 'suma' , 'error'])
#print('x \t exacta \t suma \t error')
for j in x:
    suma = j
    term = j
    for i in range(2, n):
        term = (-term *j*j)/((2*i-1)*(2*i-2))
        suma = suma + term
    t.add_row([j, math.sin(j), suma, error_relativo(j, suma)])

print(t)

