#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 17:50:18 2022

@author: gustavo
"""


import numpy as np
import matplotlib.pylab as plt
from matplotlib import cm

Nmax = 100
Niter = 70
V = np.zeros((Nmax, Nmax), float)

for i in range(100):
    for j in range(100):
        V[i][j] = 0.0

for k in range(0, Nmax-1):
    V[k,0] = 100.0

for iter in range(Niter):
    if iter%10 == 0: print(iter)
    
    for i in range(1, Nmax-2):
        for j in range(1, Nmax-2):
            V[i,j] = 0.25 * (V[i+1,j] + V[i-1,j] + V[i,j+1] + V[i,j-1])

x = range(0, Nmax-1, 2); y = range(0, 50, 2)

X, Y = plt.meshgrid(x, y)

def functz(V):
    z = V[X, Y]
    return z

Z = functz(V)



fig = plt.figure()
# ax = Axes3D(fig)
ax = fig.add_subplot(projection='3d')
surf = ax.plot_surface(X, Y, Z, rstride=2, cstride=2, linewidth=0.5, cmap=cm.coolwarm)
surf.set_clim([np.min(Z), np.max(Z)])

ax.set_zlabel('Voltaje')
ax.set_xlabel('x')
ax.set_ylabel('y')

# Para la barra lateral
cbar = fig.colorbar(surf, shrink=0.5, aspect=10, location='left')
cbar.ax.set_ylabel('Potencial eléctrico', rotation=90)
cset = ax.contourf(X,Y,Z, zdir='z', offset=-50, cmap=cm.coolwarm)

ax.set_zlim(-50, 100)

plt.savefig('plot_Ejercicio_Laplace_Potencial_01.eps', format='eps')
plt.show()