# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 13:36:28 2022

@author: gusto
"""

from moduloDiferencias import dif_adelante_h2, dif_central_puntos, dif_atras_h2
import numpy as np
from scipy import interpolate

import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['text.usetex'] = True


def voltaje(derivada_i, corriente):
    valor = 0.98 * derivada_i + 0.142 * corriente
    return valor

def etiquetas():
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Voltaje [V]')
    plt.legend(loc='best')

tiempo = [1., 1.01, 1.02, 1.03, 1.04]
corriente = [3.10, 3.12, 3.14, 3.18, 3.24]
h = 0.1
valores = []
xinterp = [1.005, 1.015, 1.025, 1.035]

derecha = dif_adelante_h2(corriente[0], corriente[1], corriente[2], h)
valores.append(voltaje(derecha, corriente[0]))
print(voltaje(derecha, corriente[0]))

for i in range(1, len(tiempo)-1):
    central = dif_central_puntos(corriente[i-1], corriente[i+1], h)
    valores.append(voltaje(central, corriente[i]))
    print(voltaje(central, corriente[i]))

izquierda = dif_atras_h2(corriente[-1], corriente[-2], corriente[-3], h)
valores.append(voltaje(izquierda, corriente[-1]))
print(voltaje(izquierda, corriente[-1]))

npuntos = np.interp(xinterp, tiempo, valores)

x0 = np.linspace(1.001, 1.04, 100)

f2 = interpolate.interp1d(tiempo, valores, kind="quadratic")
y2 = f2(x0)

plot1 = plt.figure(1)
plt.plot(tiempo, valores, 'b+', label='Puntos tabulados')
plt.title('Valores de v(t) para los puntos de la tabla')
etiquetas()

plot2 = plt.figure(2)
plt.plot(tiempo, valores, 'b+', label='Puntos tabulados')
plt.plot(xinterp, npuntos, 'r+', label='Puntos interpolados')
plt.title('Valores de v(t) para los puntos de la tabla e interpolados')
etiquetas()

plot2 = plt.figure(3)
plt.plot(tiempo, valores, 'b+', label='Puntos tabulados')
plt.plot(xinterp, npuntos, 'r+', label='Puntos interpolados')
plt.plot(x0, y2, 'k--', lw=0.7, label='Curva de interpolación')
plt.title('Valores de v(t) para los puntos y curva de interpolación')
etiquetas()

plt.show()