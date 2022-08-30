# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 12:44:18 2022

@author: gusto
"""


import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

mpl.rcParams['text.usetex'] = True

def etiquetas():
    plt.title('Relación entre la viscosidad y la temperatura')
    plt.xlabel('Temperatura')
    plt.ylabel('Viscosidad $\mu_{k}$')
    plt.axis([-5, 110, 0, 2])

temperatura = [0., 21.1, 37.8, 54.4, 71.1, 87.8, 100]
mu_k = [1.79, 1.13, 0.696, 0.519, 0.338, 0.321, 0.296]

xdatos = [10, 30, 60, 90]
ydatos = [0, 0, 0, 0]
extraticks = [10, 30, 60, 90]
x2 = np.arange(0, 100)

interp_1 = interpolate.interp1d(temperatura, mu_k, kind='linear')
y1 = interp_1(x2)

interp_2 = interpolate.interp1d(temperatura, mu_k, kind='quadratic')
y2 = interp_2(x2)

yinterp = [1.4684, 0.87286, 0.45517, 0.31905]

plot1 = plt.figure(1)
plt.plot(temperatura, mu_k, '+b')
etiquetas()

plot2 = plt.figure(2)
plt.plot(xdatos, ydatos, 'or')
plt.plot(temperatura, mu_k, '+b')
# Para generar la tercera gráfica
plt.axvline(x=10, ymin=0, ymax=0.9, ls='dashed', lw=0.7, color='r')
plt.axvline(x=30, ymin=0, ymax=0.6, ls='dashed', lw=0.7, color='r')
plt.axvline(x=60, ymin=0, ymax=0.3, ls='dashed', lw=0.7, color='r')
plt.axvline(x=90, ymin=0, ymax=0.2, ls='dashed', lw=0.7, color='r')
# ------
plt.xticks(list(plt.xticks()[0]) + extraticks)
etiquetas()

plot3 = plt.figure(3)
plt.plot(y1, color='r', label='Interp. lineal')
plt.plot(temperatura, mu_k, '+b', label='Datos')
plt.plot(xdatos, ydatos, 'ob', label='Datos interpolados')
plt.legend(loc='best')
etiquetas()

plot4 = plt.figure(4)
plt.plot(y2, color='r', label='Interp. cuadrática')
plt.plot(temperatura, mu_k, '+b', label='Datos')
plt.plot(xdatos, yinterp, 'ok', label='Datos interpolados')
plt.xticks(list(plt.xticks()[0]) + extraticks)
plt.legend(loc='best')
etiquetas()


plt.show()