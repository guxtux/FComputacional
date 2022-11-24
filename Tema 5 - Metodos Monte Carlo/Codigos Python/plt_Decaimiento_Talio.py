#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: gustavo
"""

import matplotlib.pyplot as plt
from random import random
import numpy as np

plt.rcParams['font.family'] = 'Arial'


NTl = 1000
NPb = 0
tau = 3.053*60
h = 1
p = 1 - 2**(-h/tau)
tmax = 1000

tpuntos = np.arange(0., tmax, h)
Tlpuntos = []
Pbpuntos = []

for i in tpuntos:
    Tlpuntos.append(NTl)
    Pbpuntos.append(NPb)
    
    decaimiento = 0
    
    for i in range(NTl):
        if random() < p:
            decaimiento += 1
    
    NTl -= decaimiento
    NPb += decaimiento
    
plt.plot(tpuntos, Tlpuntos, label='Talio')
plt.plot(tpuntos, Pbpuntos, label='Plomo')
plt.title('Simulación de decaimiento radiactivo')
plt.legend(loc='best')
plt.xlabel('Tiempo [s]')
plt.ylabel('Número de átomos')
plt.savefig('plot_decaimiento_radiactivo_01.eps', format='eps')
plt.savefig('plot_decaimiento_radiactivo_01.png', format='png')
plt.show()
