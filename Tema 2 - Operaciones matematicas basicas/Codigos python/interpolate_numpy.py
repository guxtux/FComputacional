# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 14:18:51 2017

@author: Master Chief
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

x = np.linspace(-18, 18, 36)
ruido = 0.1 * np.random.random(len(x))
senal = np.sinc(x) + ruido

interpreteda = interpolate.interp1d(x, senal)
x2 = np.linspace(-18, 18, 180)
y = interpreteda(x2)

cubica = interpolate.interp1d(x, senal, kind="cubic")
y2 = cubica(x2)

plt.plot(x, senal, 'o', label="datos")
plt.plot(x2, y, '-', lw=0.7, label="lineal")
plt.plot(x2, y2, '-', lw=0.7, label="cúbica")
plt.legend()
plt.show()