
import numpy as np
from ModuloPoisson import Poisson2D


def Func(x, y):
   return 0e0


def FrontCondElipse(u, imin, imax, nx, ny):
   x0 = 0.5e0*(nx + 1e0)
   y0 = 0.5e0*(ny + 1e0)
   a = x0 - 1e0
   b = y0 - 1e0

   for j in range(1,ny+1):
      yj = j - y0
      xi = a * np.sqrt(1e0 - yj*yj/(b*b))
      if (xi == 0e0): xi = 0.75e0

      imin[j] = int(x0 - xi + 0.5e0)
      imax[j] = int(x0 + xi + 0.5e0)

   for i in range(imin[1],imax[1]+1): u[i][1] = 0e0
   for j in range(2,ny):
      u[imin[j]][j] = 100e0 * (nx - 2*imin[j])/(nx-1)
      u[imax[j]][j] = 0e0
   for i in range(imin[ny],imax[ny]+1): u[i][ny] = 0e0



a = 5
xmin = -a; xmax = a; ymin = -a; ymax = a
nx = 51; ny = 51
eps = 1e-5

u = [[0]*(ny+1) for i in range(nx+1)]
x = [0]*(nx+1); y = [0]*(ny+1)
imin = [0]*(ny+1)
imax = [0]*(ny+1)

hx = (xmax-xmin)/(nx-1)
for i in range(1,nx+1): x[i] = xmin + (i-1)*hx
hy = (ymax-ymin)/(ny-1)
for j in range(1,ny+1): y[j] = ymin + (j-1)*hy

for j in range(1,ny+1):
   for i in range(1,nx+1): u[i][j] = -1e99

FrontCondElipse(u,imin,imax,nx,ny)

for j in range(2,ny):
   for i in range(imin[j]+1,imax[j]): u[i][j] = 0e0

Poisson2D(u,x,y,imin,imax,nx,ny,eps,Func)

salida = open("DiscoLaplace.txt", "w")
salida.write("x \t y \t u\n")
for j in range(1, ny+1):
   for i in range(1, nx+1):
      salida.write(("{0:10.5f} \t {1:10.5f} \t {2:14.5e}\n").format(x[i],y[j],u[i][j]))
salida.close()
