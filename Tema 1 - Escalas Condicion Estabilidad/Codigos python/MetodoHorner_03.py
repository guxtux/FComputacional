#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 13:43:34 2020

@author: gustavo
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams['text.usetex'] = True

#2 + 4 * x - 5 * x**2 + 2 * x**3 - 6 * x**4 + \
#            8 * x**5 + 10 * x**6

# Método de Horner
def funcion_horner(x):                         
    p_hor = 0
    for n in range(len(a)-1, -1, -1):     
        p_hor = a[n] + p_hor * x
    return p_hor

# Evaluación con numpy
def funcion_eval(puntos, coeficientes):
    valores = np.polynomial.polynomial.polyval(puntos, coeficientes)
    return valores

# Cálculo del error relativo
def err_rel(p, p_): return np.fabs(p - p_)/p

exacta = []
errores = []
a = [2, 4, -5, 2, -6, 8, 10]
x0 = [-1.5, -0.65, 0.1, 1.4, 2.87]
x1 = np.linspace(-2, 3)

aproximacion = funcion_eval(x0, a)

print('eval \t\t\t Horner \t\t\t Error relativo')
print('-'*50)

for i in range(len(x0)):
    exacta.append(funcion_horner(x0[i]))
    errores.append(err_rel(exacta[i], aproximacion[i]))
    print('{0:1.6e} \t {1:1.6e} \t {2:1.6e}'.format(exacta[i], aproximacion[i], errores[i]))


plt.plot(x1, funcion_eval(x1, a), label=u'Evaluación Polinomio')
plt.plot(x0, exacta, 'or', color='red', label='Método de Horner')
plt.title(u'Comparación gráfica entre el método eval y el de Horner')
plt.legend(loc='upper left')
plt.xlabel('Puntos $x_{0}$')
plt.ylabel('$P (x_{0})$')
plt.axis([-2,3,-110,7000])
plt.show()