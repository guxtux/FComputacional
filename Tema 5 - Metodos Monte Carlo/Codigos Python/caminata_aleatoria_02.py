#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: gustavo
"""

import random
import numpy as np
import matplotlib.pyplot as plt
# from scipy import stats

plt.rcParams['font.family'] = 'Arial'

p = 0.5
dx = 1
n = 100
t = 1000
x = np.zeros((n, t))


plot1 = plt.figure(1)
for i in range(n):
    x[i][0] = 0
    
    for j in range (1, t):
        if random.random() < p:
            x[i][j] = x[i][j-1] + dx
        else:
            x[i][j] = x[i][j-1] - dx

    plt.plot(x[i])

plt.title('Caminata aleatoria con n = {0:} y t = {1:}'.format(n, t))
# plt.savefig('plot_caminata_aleatoria_04.eps', format='eps')
# plt.savefig('plot_caminata_aleatoria_04.png', format='png')

# %% Celda para calcular el promedio de recorrido

media = np.mean(x, axis=0)
varianza = (np.mean(x**2, axis=0) - np.mean(x, axis=0))**2
# x2 = np.arange(0, t, 1)

plot2 = plt.figure(2)

plt.plot(media)
plt.title('Promedio de la distancia')
plt.xlabel('n')
plt.ylabel(r'$<x>$')
# plt.savefig('plot_caminata_aleatoria_05.eps', format='eps')
# plt.savefig('plot_caminata_aleatoria_05.png', format='png')

plot3 = plt.figure(3)

plt.plot(varianza)
plt.title('Varianza de la distancia')
plt.xlabel('n')
plt.ylabel(r'$\sigma$')
# plt.savefig('plot_caminata_aleatoria_06.eps', format='eps')
# plt.savefig('plot_caminata_aleatoria_06.png', format='png')

# res = stats.linregress(x2, varianza)
# print(res.intercept, res.slope)

# plot4 = plt.figure(4)
# plt.plot(x2, res.intercept + res.slope*varianza, 'r', label='fitted line')

plt.show()