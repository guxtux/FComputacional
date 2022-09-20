# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 16:25:43 2013

@author: IIFCES
"""

from moduloDiferencias import ddif_central
from tabulate import tabulate
import numpy as np

def funcion(x):
    return np.exp(-x)


lista2 = []

h = 0.64
x = 1.

cabeceras = ['h', 'derivada', 'error']

for i in range(1, 15):
    lista1 = []
    lista1.append(h)
    lista1.append(ddif_central(funcion, x, h))
    lista1.append(abs(0.36787944 - ddif_central(funcion, x, h)))
    h = h*0.5
    lista2.append(lista1)

print(tabulate(lista2, headers = cabeceras, tablefmt="grid", colalign=("decimal",), floatfmt=(".5f", ".8f", "1.6e")))