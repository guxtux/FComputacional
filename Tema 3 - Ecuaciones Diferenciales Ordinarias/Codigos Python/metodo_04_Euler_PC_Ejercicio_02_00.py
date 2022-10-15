#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 17:30:12 2022

@author: gustavo
"""

from metodosDirectos import euler
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['text.usetex'] = True


def Func_V(t, y, f):
    f[1] = y[0]
    f[2] = -k/m * y[1] * np.fabs(y[1]) - g
    
def f(x, y):
    f = np.zeros(2)
    f[0] = y[1]
    f[1] = -k/m * y[1] * np.fabs(y[1]) - g
    return f



g = 9.81e0
m = 7.26e0
R = 0.06e0
x0 = 0e0
y0 = 2e0

phi = 45e0 * np.pi/180e0

rho = 1.2
Cd = 0.5e0
k = 0.5e0 * rho * (np.pi * R * R) * Cd
tmax = 100e0
ht = 0.01e0

n = 2
nt = int(tmax/ht + 0.5) + 1

y = np.zeros(n+1)
tt = np.zeros(nt+1)
xt = np.zeros(nt+1)
yt = np.zeros(nt+1)

t = 0e0
it = 1

y[1] = x0 
y[2] = y0

tt[1] = t
xt[1] = y[1]
yt[1] = y[2]


# ---- Solución con el método de Euler ----

# while (t + ht <= tmax):
#     euler2(t, ht, y, n, Func_V)
#     t += ht
#     it += 1
   
#     tt[it] = t
#     xt[it] = y[1]
#     yt[it] = y[2]
   
#     if (y[2] < 0.e0): break

x = 0.0
xAlto = 5.0
y = np.array([2., 0.])
h = 0.01

X, Y = euler(f, x, y, xAlto, h)

plt.plot(X, Y[:,1])
plt.show()