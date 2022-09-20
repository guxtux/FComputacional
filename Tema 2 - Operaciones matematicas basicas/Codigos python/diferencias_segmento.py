#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 21:09:25 2022

@author: gustavo
"""

from moduloDiferencias import dif_adelante_h2, dif_central_puntos, dif_atras_h2
from tabulate import tabulate
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['text.usetex'] = True

# from matplotlib import rc
# # rc("pdf", fonttype=3)
# # rc('font',**{'family':'serif'})
# rc('text', usetex=True)
# plt.rcParams.update({
# "text.usetex": True,
# "font.family": "sans-serif",
# "font.sans-serif": ["Helvetica"]})

def etiquetas():
    plt.title('Velocidad angular del segmento AB')
    plt.xlabel('Ángulo en grados')
    plt.ylabel('Velocidad en rad/s')
    plt.legend(loc='best')
    plt.xlim([-0.5, 30.5])


alfa = [0., 5., 10., 15., 20., 25., 30.]
beta = [1.6595, 1.5434, 1.4186, 1.2925, 1.1712, 1.0585, 0.9561]
h = 0.087266

lista1 = []
lista3 = []
totales = []
y = []

izquierda = 25 * dif_adelante_h2(beta[0], beta[1], beta[2], h)
lista1.append(0)
lista1.append(izquierda)
totales.append(lista1)

for i in range(1, len(alfa)-1):
    lista2 = []
    aproximacion = dif_central_puntos(beta[i-1], beta[i+1], h)
    velocidad = 25 * aproximacion
    lista2.append(alfa[i])
    lista2.append(velocidad)
    totales.append(lista2)

derecha = 25 * dif_atras_h2(beta[-1], beta[-2], beta[-3], h)
lista3.append(30)
lista3.append(derecha)
totales.append(lista3)

cabeceras = ['alfa', 'beta']

print(tabulate(totales, headers = cabeceras, tablefmt="grid", stralign="center", floatfmt=("", ".6f")))

# ------- Rutina para recuperar el valor de velocidad angular

for i in range(len(totales)):
    y.append(totales[i][1])

# ------- Rutina para interpolación ----------

x0 = np.linspace(0.1, 30, 100)

f2 = interpolate.interp1d(alfa, y, kind="quadratic")
y2 = f2(x0)

#------- Rutina para graficación ----------

plot1 = plt.figure(1)
plt.plot(alfa, y, '+r', label='Aproximación derivada')
etiquetas()

plot2 = plt.figure(2)
plt.plot(alfa, y, '+r', label='Aproximación derivada')
plt.plot(x0, y2, label='Curva de interpolación')
etiquetas()

plt.show()