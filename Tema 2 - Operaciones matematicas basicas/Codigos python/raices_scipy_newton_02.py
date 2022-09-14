# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 17:53:20 2017

@author: Master Chief
"""

import scipy.optimize
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    y = x + 2 * np.cos(x)
    return y

def etiquetas():
    plt.grid(True)
    plt.xlim([-5, 5])
         
raiz= scipy.optimize.newton(f,  2, fprime=lambda x: 1 - 2 * np.sin(x))

print('La raíz de la función es = {0:1.5f}'.format(raiz))

x = np.linspace(-5, 5)

plot1 = plt.figure(1)
plt.plot(x, f(x))
plt.title('Función f(x) a la que se desea calcular la raíz')
etiquetas()

cadena1 = r'$x_0 = {0:1.5}$'.format(raiz)
plot2 = plt.figure(2)
plt.plot(x, f(x), label='Función f(x)')
plt.plot(raiz, 0,'bo', label='Raíz calculada')
plt.text(-1, -1, cadena1, fontsize=14)
plt.title('Raíz obtenida con optimize.newton')
plt.legend(loc='best')
etiquetas()

plt.show()