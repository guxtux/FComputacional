# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 14:44:40 2022

@author: gusto
"""

from moduloAleatorio import int3areaMC
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(-(x**2)/2)/np.sqrt(2*np.pi)

x = np.linspace(0, 5)

k, I = int3areaMC(f, 0, 4, 100, f(4))

plt.plot(x, f(x))
plt.plot(k, I, 'b+')
plt.show()
