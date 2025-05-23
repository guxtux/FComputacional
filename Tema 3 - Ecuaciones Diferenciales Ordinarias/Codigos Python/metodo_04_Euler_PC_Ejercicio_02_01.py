#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 12:56:39 2022

@author: gustavo
"""

from metodosDirectos import eulerPC
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['text.usetex'] = True


def Func(t, y, f):
   f[1] = y[3]
   f[2] = y[4]
   f[3] = -k/m * y[3]*np.fabs(y[3])
   f[4] = -k/m * y[4]*np.fabs(y[4]) - g

g = 9.81e0
m = 7.26e0
R = 0.06e0
x0=0e0
y0=2e0
v0 = 25e0
phi = 45e0 * np.pi/180e0
vx0 = v0 * np.cos(phi)
vy0 = v0 * np.sin(phi)
rho = 1.2
Cd = 0.5e0
k = 0.5e0 * rho * (np.pi * R * R) * Cd
tmax = 20e0
ht = 0.01e0

n = 4
nt = int(tmax/ht + 0.5) + 1

y = [0] * (n+1)
tt = [0] * (nt+1)
xt = [0] * (nt+1)
yt = [0] * (nt+1)

t = 0e0
it = 1

y[1] = x0 
y[2] = y0
y[3] = vx0
y[4] = vy0

tt[1] = t
xt[1] = y[1]
yt[1] = y[2]


# ---- Solución con el método de Euler ----

while (t + ht <= tmax):
   eulerPC(t, ht, y, n, Func)
   t += ht
   it += 1
   
   tt[it] = t
   xt[it] = y[1]
   yt[it] = y[2]
   
   if (y[2] < 0.e0): break

print('Método de Euler\n')
print('xmax = {0:5.2f} m'.format(y[1]))

hmax = np.argmax(yt)

print('hmax = {0:3.2f} m'.format(yt[hmax]))

# %% Ejecuta la primera gráfica

plot1 = plt.figure(1)
plt.plot(xt[:it], yt[:it])
plt.plot(y[1], 0, 'ok')
plt.title('Distancia máxima alcanzada en el lanzamiento - Euler')
plt.xlabel('x')
plt.ylabel('y')
plt.text(60, 5, r'xmax = {0:5.2f} m'.format(y[1]))
plt.xlim([0, 70])
plt.axhline(y=0, ls='dashed', lw=0.7, color='k')

print(len(yt))

# %% Ejecuta la segunda gráfica
plot2 =plt.figure(2)
plt.plot(tt[:it], yt[:it])
plt.plot(tt[hmax], yt[hmax], 'or')
plt.text(1.7, 20, r'hmax = {0:3.2f} m'.format(yt[hmax]))
plt.title('Altitud alcanzada')
plt.xlabel('t')
plt.ylabel('y')
plt.xlim([0, 4])
plt.axhline(y=0, ls='dashed', lw=0.7, color='k')

plt.show()