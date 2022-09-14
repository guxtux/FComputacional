# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 20:14:32 2020

@author: gusto
"""

from moduloRaices import buscaraiz
from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['text.usetex'] = True



def f(x):
    return (x**2 - 1)

def ejes():
    plt.grid(True)
    # plt.axhline(y=0, ls='dashed', lw=0.7, color='k')
    # plt.axvline(x=0, ls='dashed', lw=0.7, color='k')
    plt.axis([-2, 2, -2, 4])

a, b, dx = -2., 2., 0.1

x0 = np.linspace(-2, 2, 100)

intervalo1 = []
intervalo2 = []
raices = []

inicio = a
final = 0.

a1, b1 = buscaraiz(f, inicio, final, dx)

inicio = final
final = b
a2, b2 = buscaraiz(f, inicio, final, dx)

raiz1 = optimize.bisect(f, a1, b1)
raiz2 = optimize.bisect(f, a2, b2)

print('La raíz está en x = {0:1.6f}'.format(raiz1))
print('La raíz está en x = {0:1.6f}'.format(raiz2))

raices.append(raiz1)
raices.append(raiz2)

plot1 = plt.figure(1)
plt.plot(x0, f(x0))
ejes()
plt.title('Grafica de la función f(x) en el intervalo')

cadena1 = r'$x_0 = {0:1.3f}$'.format(raices[0])
cadena2 = r'$x_1 = {0:1.3f}$'.format(raices[1])

plot2 = plt.figure(2)
plt.plot(x0, f(x0))
plt.plot(raices[0], 0, 'ro')
plt.plot(raices[1], 0, 'ro')
plt.text(-1, 0.5, cadena1, fontsize=14)
plt.text(0.5, 0.5, cadena2, fontsize=14)
plt.title('Raíces de la función usando optimize.bisect', style='italic')
ejes()


plt.show()