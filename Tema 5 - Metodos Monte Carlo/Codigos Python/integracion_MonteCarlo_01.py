#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: gustavo
"""

from moduloAleatorio import intMC

def f(x):
    return 2 + 3*x

integral = intMC(f, 1, 2, 100)

print('Valor de la integral: {0:}'.format(integral))
print('Error absoluto: {0:1.5e}'.format(6.5 - integral))