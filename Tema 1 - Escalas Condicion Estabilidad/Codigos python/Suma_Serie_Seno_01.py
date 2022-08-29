#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 16:17:25 2020

@author: gustavo
"""

import matplotlib as mpl
import math
import matplotlib.pyplot as plt
mpl.rcParams['text.usetex'] = True

def error_relativo(exacto, aproximado):
    return math.fabs(math.sin(exacto)- aproximado)/math.sin(exacto)*100

def etiquetas():
    plt.xlabel('Iteración')
    plt.ylabel('Error relativo')

a = float(input('Teclea el valor a evaluar: '))
x = math.radians(a)


j = 0
n = 10
suma = x
term =  x
error = []
eje_x = range(2, n)

print('El valor de sen ({0:}) = {1:1.10f} \n'.format(a, math.sin(x)))
      
print('Iteracion  Aproximacion \t Error')
print('-'*45)
      
for i in range(2, n):
    j += 1
    term = (-term * x * x)/((2 * i - 1) * (2 * i - 2))
    suma  = suma + term
    print('{0:} \t {1:1.10f} \t {2:1.5e}'.format(j, suma, error_relativo(x, suma)))
    error.append(error_relativo(x,  suma))


plot1 = plt.figure(1)
plt.plot(eje_x, error, '+')
plt.plot(eje_x, error, ls='dashed', lw=0.7, color='red')
plt.title('Error relativo al calcular $sin (x)$')
etiquetas()

plot2 = plt.figure(2)
plt.semilogy(eje_x, error, '+')
plt.semilogy(eje_x, error, ls='dashed', lw=0.7, color='red')
plt.title('Error relativo al calcular $sin (x)$ con el eje y - logarítmico')
etiquetas()

plt.show()
