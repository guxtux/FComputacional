#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 20:14:43 2022

@author: gustavo
"""

from metodoRidder import ridder
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['text.usetex'] = True

def f(x):
    a = (x - 0.3)**2 + 0.01
    b = (x - 0.8)**2 + 0.04
    
    return 1./a - 1./b

def etiquetas():
    plt.grid(1)
    plt.xlim(-2, 3)
    plt.ylim(-27, 100)
    
raiz = ridder(f, 0., 1.)
print('La raíz es: {0:}'.format(raiz))

x = np.linspace(-2, 3, 500)

# %% Primera imagen
plot1 = plt.figure(1)
plt.plot(x, f(x))
plt.title('Gráfica inicial para determinar el intervalo de la raíz')
etiquetas()
plt.savefig('plot_Metodo_Ridder_Ejercicio_02_01.png', format='png')
plt.savefig('plot_Metodo_Ridder_Ejercicio_02_01.eps', format='eps')

# %% Segunda imagen
plot2 = plt.figure(2)
plt.plot(x, f(x))
plt.plot(raiz, 0, 'ro')
plt.title('La raíz está en x = {0:}'.format(raiz))
etiquetas()
plt.savefig('plot_Metodo_Ridder_Ejercicio_02_02.png', format='png')
plt.savefig('plot_Metodo_Ridder_Ejercicio_02_02.eps', format='eps')

plt.show()



