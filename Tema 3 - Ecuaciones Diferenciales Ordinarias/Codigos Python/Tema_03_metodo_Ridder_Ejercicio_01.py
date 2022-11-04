#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 19:52:24 2022

@author: gustavo
"""

from metodoRidder import ridder
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['text.usetex'] = True

def f(x):
    return x**3 - 10 * x**2 + 5

def etiquetas1():
    plt.axhline(y=0, lw=0.7, ls='dashed', color='k')    

def etiquetas2():
    plt.axvline(x=0.6, ymin=0, ymax=0.77, lw=0.7, ls='dashed', color='r')
    plt.axvline(x=0.8, ymin=0, ymax=0.32, lw=0.7, ls='dashed', color='r')

x1 = 0.6
x2 = 0.8

x = np.linspace(-1, 1)
x_inter = np.linspace(0.5, 0.9)

raiz = ridder(f, x1, x2)
print('La raíz es: {0:1.4f}'.format(raiz))

# %% Primera imagen
plot1 = plt.figure(1)
plt.plot(x, f(x))
plt.title('Gráfica de la función en un intervalo más amplio')
etiquetas1()
# plt.savefig('plot_Metodo_Ridder_Ejercicio_01_01.png', format='png')
# plt.savefig('plot_Metodo_Ridder_Ejercicio_01_01.eps', format='eps')

# %% Segunda imagen
plot2 = plt.figure(2)
plt.plot(x_inter, f(x_inter))
plt.title('Intervalo donde se indica que existe una raíz de la función')
etiquetas1()
etiquetas2()
# plt.savefig('plot_Metodo_Ridder_Ejercicio_01_02.png', format='png')
# plt.savefig('plot_Metodo_Ridder_Ejercicio_01_02.eps', format='eps')

# %% Tercera imagen
plot3 = plt.figure(3)
plt.plot(x_inter, f(x_inter))
plt.plot(raiz, 0, 'or')
plt.title('Valor de la raíz en el intervalo es = {0:1.4}'.format(raiz))
etiquetas1()
etiquetas2()
# plt.savefig('plot_Metodo_Ridder_Ejercicio_01_03.png', format='png')
# plt.savefig('plot_Metodo_Ridder_Ejercicio_01_03.eps', format='eps')

plt.show()