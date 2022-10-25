#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 21:17:06 2022

@author: gustavo
"""
from metodosDirectos import eulerPC
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['text.usetex'] = True

def Func(t, y, f):
   f[0] = y[2]
   f[1] = y[3]
   f[2] = -k/m * y[2]*np.fabs(y[2])
   f[3] = -k/m * y[3]*np.fabs(y[3]) - g

g = 9.81e0
m = 7.26e0
R = 0.06e0
x0=0e0
y0=3e0
v0 = 29e0
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

y = np.zeros(n+1)
tt = np.zeros(nt+1)
xt = np.zeros(nt+1)
yt = np.zeros(nt+1)

t = 0e0
it = 1

y[0] = x0
y[1] = y0
y[2] = vx0
y[3] = vy0

tt[0] = t
xt[0] = y[0]
yt[0] = y[1]


salida = open('valores_CD_05.txt', 'w')
    
salida.write("{0:2.5f} {1:2.5f} {2:1.5f}\n".format(tt[1], xt[1], yt[1]))


# ---- Solución con el método Predictor-Corrector de Euler ----

while (t + ht <= tmax):
    eulerPC(t, ht, y, n, Func)
    t += ht
    it += 1
   
    tt[it] = t
    xt[it] = y[0]
    yt[it] = y[1]
    salida.write("{0:2.5f} {1:2.5f} {2:1.5f}\n".format(tt[it], xt[it], yt[it]))
   
    if (y[1] < 0.e0): break

print(r'Método de Euler Predictor-Corrector con $C_{D} = 0.5$')
print('\nxmax = {0:5.2f} m'.format(y[0]))

hmax = np.argmax(yt)

print('hmax = {0:3.2f} m'.format(yt[hmax]))

salida.close()

plot1 = plt.figure(1)
plt.plot(xt[:433], yt[:433])
plt.plot(y[0], 0, 'ok')
plt.title('Distancia máxima alcanzada en el lanzamiento $C_{D}= 0.5$ - Euler PC')
plt.xlabel('x')
plt.ylabel('y')
plt.text(60, 5, r'xmax = {0:5.2f} m'.format(y[0]))
plt.xlim([0, 90])
plt.axhline(y=0, ls='dashed', lw=0.7, color='k')
#plt.savefig('plot_eulerPC_ejercicio_02_01.eps', format='eps')
#plt.savefig('plot_eulerPC_ejercicio_02_01.png', format='png')

plot2 =plt.figure(2)
plt.plot(tt[:433], yt[:433])
plt.plot(tt[hmax], yt[hmax], 'or')
plt.text(1.7, 20, r'hmax = {0:3.2f} m'.format(yt[hmax]))
plt.title('Altitud alcanzada $C_{D}= 0.5$ - Euler PC')
plt.xlabel('t')
plt.ylabel('y')
plt.xlim([0, 4.5])
plt.axhline(y=0, ls='dashed', lw=0.7, color='k')
#plt.savefig('plot_eulerPC_ejercicio_02_02.eps', format='eps')
#plt.savefig('plot_eulerPC_ejercicio_02_02.png', format='png')

plt.show()