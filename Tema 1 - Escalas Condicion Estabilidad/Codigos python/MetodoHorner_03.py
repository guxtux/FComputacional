#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 13:43:34 2020

@author: gustavo
"""

import numpy as np

#2 + 4 * x - 5 * x**2 + 2 * x**3 - 6 * x**4 + \
#            8 * x**5 + 10 * x**6

#los coeficientes se ingresan de la potencia menor de x a la potencia mayor
a = [2, 4, -5, 2, -6, 8, 10]

x0 = [-1.5, -0.65, 0.1, 1.4, 2.87]

#la funcion polival requiere que las potencias de x, se ingresen de la mayor
#a la menor, por ello se ocupa la función reverse
a.reverse()

print ('Potencias del polinomio en orden inverso')
print(a)
print()


for i in x0:
    valor = np.polyval(a, i)
    print(valor)
    