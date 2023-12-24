import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


kappa = 210.
sph = 900.
rho = 2700.

Nx = 101
Nt = 3000
Dx = 0.01414                                                
Dt = 1.

cons = kappa/(sph*rho)*Dt/(Dx*Dx)

T = np.zeros((Nx, 2), dtype=float)
Tpl = np.zeros ((Nx, 31), dtype=float)

for ix in range(1, Nx-1):
    T[ix, 0] = 100.0

T[0, 0] = 0.0
T[0, 1] = 0.0

T[Nx-1, 0] = 0.0
T[Nx-1, 1] = 0.0
m = 1

for t in range(1, Nt):
    for ix in range(1, Nx-1):
        T[ix, 1] = T[ix,0] + cons*(T[ix+1,0] + T[ix-1,0] - 2.*T[ix,0])
    if t%100 == 0 or t == 1:
        for ix in range(1,Nx-1,2):
            Tpl[ix,m] = T[ix,1]
        print (m)
        m = m+1
    for ix in range(1, Nx-1):
        T[ix,0] = T[ix,1]

x = list(range(1, Nx-1, 2))
y = list(range(1, 30))

X, Y = np.meshgrid(x,y)

def functz(Tpl):
    z = Tpl[X,Y]
    return z
    
Z = functz(Tpl)

fig = plt.figure()
#ax = Axes3D(fig)
ax = fig.add_subplot(projection='3d')
surf = ax.plot_surface(X,Y,Z,rstride=1,cstride=1,linewidth=0.5,cmap=cm.hot_r)

ax.set_zlim(-50, 100)

cset = ax.contourf(X,Y,Z,zdir='z',offset=-50,cmap=cm.hot_r)
cbar = fig.colorbar(surf,shrink=0.5,aspect=5)
cbar.ax.set_ylabel('Temperatura',rotation=270,labelpad=10)
ax.set_xlabel('Posicion')
ax.set_ylabel('Tiempo')
plt.title('Grafica obtenida con el algoritmo para la ecuacion de calor')
plt.show()

