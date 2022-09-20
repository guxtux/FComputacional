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
    plt.xlabel(r'Ángulo $\alpha$ en grados')
    plt.ylabel('Velocidad en rad/s')
    plt.legend(loc='best')
    plt.xlim([-0.5, 30.5])


alfa = [0., 5., 10., 15., 20., 25., 30.]
beta = [1.6595, 1.5434, 1.4186, 1.2925, 1.1712, 1.0585, 0.9561]
h = 0.087266

xinterp =[2.5, 7.5, 12.5, 17.5, 22.5, 27.5]

lista1 = []
lista3 = []
totales = []
y = []

# -------- Cálculo de las derivadas en los extremos y puntos centrales

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

# ------- Rutina para obtener puntos interpolados -----

npuntos = np.interp(xinterp, alfa, y)

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
plt.plot(xinterp, npuntos, '+b', label='Puntos interpolados')
etiquetas()

plot2 = plt.figure(3)
plt.plot(alfa, y, '+r', label='Aproximación derivada')
plt.plot(xinterp, npuntos, '+b', label='Puntos interpolados')
plt.plot(x0, y2, '--k', lw=0.7, label='Curva de interpolación')
etiquetas()

plt.show()