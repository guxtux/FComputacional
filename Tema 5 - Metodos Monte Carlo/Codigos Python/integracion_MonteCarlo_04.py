#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: gustavo
"""
from moduloAleatorio import intareaMC, intareavecMC, int3areaMC
import time

def f(x):
    return 2 + 3 * x

def error(aprox):
    return abs((6.5-aprox)/6.5)

a = 1; b = 2; n = 1000000; N = 10000; fmax = f(b)

t0 = time.process_time()

valor1 = intareaMC(f, a, b, n, fmax)
print('Integral = {0:}'.format(valor1))
print('Error: {0:1.5e}'.format(error(valor1)))

t1 = time.process_time()

print('Tiempo en bucle: {0} segundos'.format(t1 - t0))

valor2 = intareavecMC(f, a, b, n, fmax)
print('\nIntegral = {0:}'.format(valor2))
print('Error: {0:1.5e}'.format(error(valor2)))

t2 = time.process_time()
print('Tiempo en vectorizada: {0} segundos'.format(t2 - t1))

print ('\nFracción bucle/vectorizada: {0:}'.format((t1 - t0)/(t2 - t1)))

k, I = int3areaMC(f, a, b, n, fmax, N)

print('\nIntegral = {0:}'.format(I[-1]))
print('Error: {0:1.5e}'.format(error(I[-1])))
