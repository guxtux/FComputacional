# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 21:09:48 2020

@author: gusto
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data01 = np.loadtxt('DiscoLaplace.txt', delimiter='\t', skiprows=1)

X, Y, Z = data01[:,0], data01[0:,1], data01[:,2]

x, y = np.meshgrid(X, Y)
plt.plot(x,y)
#fig = plt.figure()
#fig = plt.figure(figsize=(8,5)) #Para incluir la barra de color
#ax = Axes3D(fig)
#surf = ax.plot_trisurf(X, Y, Z, cmap=plt.cm.jet, lw=0.1)
#ax.plot_trisurf(X, Y, Z, cmap=plt.cm.jet, lw=0.1)
#plt.contour(x, y, Z)
#ax.dist=12
#ax.view_init(30, 45)
#ax.set_xlabel('Eje X')
#ax.set_ylabel('Eje Y')
#ax.set_zlabel('Eje Z')
#ax.set_title('Solución a la ec. de Laplace')
#fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()
























