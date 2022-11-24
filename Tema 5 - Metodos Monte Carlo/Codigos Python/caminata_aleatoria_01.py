#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: gustavo
"""

import random
import matplotlib.pyplot as plt


p = 0.5
dx = 1
t = 10000
x = [t]
x[0] = 0

for i in range(1, t-1):
    if random.random() < p:
        x.append(x[i-1] + dx)
    else:
        x.append(x[i-1] - dx)

plt.plot(x)
# plt.savefig('plot_caminata_aleatoria_01.eps', format='eps')
# plt.savefig('plot_caminata_aleatoria_01.png', format='png')
plt.show()
