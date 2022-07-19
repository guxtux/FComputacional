# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 14:27:51 2017

@author: Master Chief
"""

import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

font_path = 'C:\Windows\Fonts\consola.ttf'
font_prop = font_manager.FontProperties(fname=font_path, size=10)

title_font = {'fontname':'Arial', 'size':'16', 'color':'black', 'weight':'normal',
              'verticalalignment':'bottom'}

# Setting up fake data
x = np.linspace(0, 10 * np.pi, 20)
y = np.cos(x)
# Interpolating data
fl = interp1d(x, y, kind='linear')
fq = interp1d(x, y, kind='quadratic')
# x.min and x.max are used to make sure we do not
# go beyond the boundaries of the data for the
# interpolation.
xint = np.linspace(x.min(), x.max(), 1000)
yintl = fl(xint)
yintq = fq(xint)

plt.plot(x,y, 'bo', label='Datos')
plt.plot(xint, yintl, label='Lineal')
plt.plot(xint, yintq, label='Cúbica')
plt.legend(bbox_to_anchor=(1, 0.5), loc='center left', prop=font_prop)
plt.title('Comparación entre tipos de interpolación',**title_font)
plt.show()