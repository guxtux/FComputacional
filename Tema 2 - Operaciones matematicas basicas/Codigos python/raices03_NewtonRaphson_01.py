# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 12:16:44 2012

@author: Gustavo
"""

from moduloRaices import newtonRaphson1
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['text.usetex'] = True

def f(x): return x**4 - 6.4*x**3 + 6.45*x**2 + 20.538*x - 31.752

def df(x): return 4.0*x**3 - 19.2*x**2 + 12.9*x + 20.538

def etiquetas():
    plt.title('Gráfica de f(x)')
    plt.grid(True)

raiz, numIter = newtonRaphson1(2.0, f, df)

print('La raíz es = {0:1.5f}'.format(raiz))
print('Número de iteraciones realizadas = {0:}'.format(numIter))

x = np.linspace(0, 5, 200)

plot1 = plt.figure(1)
plt.plot(x, f(x))
plt.axis([0, 5, -30, 60])
etiquetas()

plot2 = plt.figure(2)
plt.plot(x, f(x), label='Función f (x)')
plt.plot(raiz, f(raiz), 'or', label='Raiz ' + str(round(raiz, 5)))
plt.axis([1.9, 2.3, -1, 1])
plt.legend(loc='best')
etiquetas()

plt.show()