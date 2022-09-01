#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 17:36:20 2022

@author: gustavo
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

mpl.rcParams['text.usetex'] = True

x = np.array([0.0, 1., 2., 2.5, 3.])
y = np. array([2.9, 3.7, 4.1, 4.4, 5.0])

x1 = np.linspace(0, 3)

A = np.vstack([x, np.ones(len(x))]).T

m, c = np.linalg.lstsq(A, y, rcond=None)[0]

interp_1 = interpolate.interp1d(x, y, kind='quadratic')
y1 = interp_1(x1)

print(m, c)

plot1 = plt.figure(1)
plt.plot(x, y, '+b', label='Datos')
plt.legend(loc='best')

plot2 = plt.figure(2)
plt.plot(x, y, '+b', label='Datos')
plt.plot(x, m*x + c, 'r', ls='dashed', label='Línea ajustada')
plt.legend(loc='best')

plot3 = plt.figure(3)
plt.plot(x, y, '+b', label='Datos')
plt.plot(x, m*x + c, 'r', ls= 'dashed', label='Línea ajustada')
plt.plot(x1, y1, 'k', label='Interpolación')
plt.legend(loc='best')

plt.show()