#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 15:46:53 2022

@author: gustavo
"""

from metodosDirectos import integra_RKAdaptativo
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['text.usetex'] = True

def F(x, y):
   F = np.zeros(2)
   F[0] = y[1]
   F[1] = -9.80665 + 65.351e-3 * y[1]**2 * np.exp(-10.53e-5*y[0])
   return F

x = 0.0
xAlto = 10.0
y = np.array([9000, 0.0])
h = 0.5

X, Y = integra_RKAdaptativo(F, x, y, xAlto, h ,1.0e-2)

print('Datos a los 10 segundos de caída:\n')
print('La altura es {0:4.2f} metros'.format(Y[:,0][-1]))
print('\nLa velocidad es {0:2.3f} m/s'.format(np.fabs(Y[:,1][-1])))

plt.plot(X, Y[:,0])
plt.plot(10, Y[:,0][-1], 'ro')
plt.title('Gráfica a los 10 segundos de la caída libre')
plt.xlabel('Tiempo [s]')
plt.ylabel('Altura [m]')
plt.ylim([8825, 9010])
plt.text(6, 8950, 'La altura es {0:4.2f} metros'.format(Y[:,0][-1]))
plt.text(6, 8925, 'La velocidad es {0:2.3f} m/s'.format(np.fabs(Y[:,1][-1])))
# plt.savefig('Ejercicio_RKAdaptativo_01.png', format='png')
plt.savefig('Ejercicio_RKAdaptativo_01.eps', format='eps')
plt.show()