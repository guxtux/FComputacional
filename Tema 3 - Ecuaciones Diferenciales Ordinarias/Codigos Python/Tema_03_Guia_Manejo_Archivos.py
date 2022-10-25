#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 13:47:46 2022

@author: gustavo
"""

import numpy as np
import csv
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['text.usetex'] = True


coeficientes1 = [1, 2, 3]
coeficientes2 = [1, 2, -3]


x = np.linspace(-10, 10)
y1 = np.polynomial.polynomial.polyval(x, coeficientes1)
y2 = np.polynomial.polynomial.polyval(x, coeficientes2)

valores = open('datos_ejercicio.dat','w')
print('\n Se ha abierto el archivo de datos para escribir.')

valores.write('{0:} \t {1:} \t {2:}\n'.format('x', 'y1', 'y2'))

for i in range(len(x)):
    valores.write('{0:2.2f} \t {1:1.3f} \t {2:1.3f}\n'.format(x[i], y1[i], y2[i]))
    
valores.close()
print('\nSe ha cerrado el archivo de datos.')

# %% Lectura del archivo de datos y rutina de graficación 

x_archivo = []
y1_archivo = []
y2_archivo = []

datos = np.loadtxt('datos_ejercicio.dat', delimiter='\t', skiprows=1)

for i in range(len(datos[:,0])):
    x_archivo.append(datos[:,0][i])
    y1_archivo.append(datos[:,1][i])
    y2_archivo.append(datos[:,2][i])

plt.plot(x_archivo, y1_archivo, label=r'$f (x) = x^{3} + x^{2} + 1$')
plt.plot(x_archivo, y2_archivo, 'r', label=r'$g (x) = -x^{3} + x^{2} + 1$')
plt.title('Gráfica de los puntos del archivo de datos')
plt.legend(loc='best')
# plt.savefig('Tema_03_Guia_Manejo_Archivos.png', format='png')
plt.show()
