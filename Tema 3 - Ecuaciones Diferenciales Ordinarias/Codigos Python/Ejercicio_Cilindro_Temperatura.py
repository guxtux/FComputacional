# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 14:43:18 2022

@author: gusto
"""

from numpy import zeros, ones, arange
from moduloMatrices import LUdescomp3, LUsoluc3
from math import log
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['text.usetex'] = True

def equations(x, h, m):
    # h2 = h*h
    d = ones(m + 1)*(-2.0)
    c = zeros(m)
    e = zeros(m)
    
    for i in range(m):
        c[i] = 1.0 - h/2.0/x[i+1]
        e[i] = 1.0 + h/2.0/x[i]
    
    b = zeros(m+1)
    d[0] = 1.0
    d[m] = 1.0
    b[m] = 200.0
    c[m-1] = 0.0
    e[0] = 0.0
    
    return c, d, e, b

xStart = 0.5 # x at left end
xStop = 1.0 # x at right end
m = 20 # Number of mesh spaces
h = (xStop - xStart)/m
x = arange(xStart,xStop + h,h)

c, d, e, b = equations(x, h, m)
# print('h = {0:}'.format(h))
# print()
# print(d)
# print()
# print(e)
# print()
# print(c)
# print()
# print(b)


c, d, e = LUdescomp3(c, d, e)
y = LUsoluc3(c,d,e,b)
# Analytical solution
y_anal = zeros(m+1)

for i in range(m+1):
    y_anal[i] = 200*(1.0 - log(x[i])/log(0.5))

plt.plot(x, y, 'r--', lw=0.7, label='Exacta')
plt.plot(x, y_anal, '+b', label='Aproximación')
plt.title('Perfil de temperaturas para el cilindro con m = {0:}'.format(str(m)))
plt.xlabel('r')
plt.ylabel('Temperatura')
plt.legend(loc='best')
plt.savefig('plot_Solucion_Cilindro_Temperaturas.eps', format='eps')
plt.show()

