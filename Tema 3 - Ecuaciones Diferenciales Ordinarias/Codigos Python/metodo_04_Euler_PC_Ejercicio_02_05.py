#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 20:18:45 2022

@author: gustavo
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['text.usetex'] = True

ejex = np.loadtxt('valores_CD_075.txt')[:,1]

col_CD0 = np.loadtxt("valores_CD_0.txt")[:, 2]

col_CD5 = np.loadtxt("valores_CD_05.txt")[:, 2]

col_CD75 = np.loadtxt("valores_CD_075.txt")[:, 2]

print(ejex)

print('CD0')
print(len(col_CD0[:431]))

print('\nCD_5')
print(len(col_CD5[:431]))

print('\nCD_75')
print(len(col_CD75))

plt.plot(ejex, col_CD0[:431])
plt.plot(ejex, col_CD5[:431])
plt.plot(ejex, col_CD75)
plt.xlabel('x')
plt.ylabel('y')
plt.xlim([0, 90])
plt.axhline(y=0, ls='dashed', lw=0.7, color='k')

plt.show()