# -*- coding: utf-8 -*-
"""
Created on Mon May  4 17:00:41 2020

@author: gusto
"""

import numpy as np
import matplotlib.pyplot as plt
from metodosDirectos import Euler

def Func(t, y, f):
   f[1] =  y[2]
   f[2] = -y[1]

y0 = 0e0; dy0 = 1e0
tmax = 100e0
ht = 0.05e0

n = 2
y = [0]*(n+1)

salida = open("edoeuler.txt","w")
salida.write("t \t y1 \t y2 \t revisa\n")

t = 0e0
y[1] = y0; y[2] = dy0

salida.write(("{0:10.5f} \t {1:10.5f} \t {2:10.5f} \t {3:10.5f}\n"). \
          format(t, y[1], y[2], y[1]*y[1]+y[2]*y[2]))

while (t+ht <= tmax):
   Euler(t, ht, y, n, Func)
   t += ht

   salida.write(("{0:10.5f} \t {1:10.5f} \t {2:10.5f} \t {3:10.5f}\n"). \
          format(t, y[1], y[2], y[1]*y[1]+y[2]*y[2]))
salida.close()

data = np.loadtxt('edoeuler.txt', delimiter='\t', skiprows=1)

plt.plot(data[:,1], data[:,2])
plt.title('Gráfica del espacio fase con el método de Euler')
plt.xlabel('$y_{2}$')
plt.ylabel('$y_{1}$')
plt.show()