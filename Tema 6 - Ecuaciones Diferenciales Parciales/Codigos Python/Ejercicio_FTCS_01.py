import matplotlib.pyplot as plt
import numpy as np

def PropagFTCS(u0, u, nx, D, hx,ht):

   lam = D*ht/(hx*hx) 
   lam1 = 1e0 - 2e0*lam

   u[1] = u0[1]
   u[nx] = u0[nx]
   
   for i in range(2, nx):
      u[i] = lam*u0[i-1] + lam1*u0[i] + lam*u0[i+1]
      
   return u

def Init(u, x, nx):
   global L
   for i in range(1, nx+1):
       u[i] = np.sin(np.pi * x[i]/L)

D = 0.1e0
L = 1e0
nx = 21
tmax = 6.0e0
ht = 1.25e-2

u0 = [0]*(nx+1)
u = [0]*(nx+1)
x = [0]*(nx+1)
hx = L/(nx-1)

for i in range(1, nx+1):
    x[i] = (i-1)*hx

Init(u0, x, nx)

t = 0e0

while (t < tmax):
   t += ht
   PropagFTCS(u0, u, nx, D, hx, ht)
   for i in range(1,nx):
       u0[i] = u[i]                  

f = np.exp(-np.pi*np.pi*D*t/(L*L))

exacta = []

for i in range(nx+1):
   exacta.append(f * np.sin(np.pi*x[i]/L))

plt.plot(x, u, 'r', label='FTCS', ls='dashed')
plt.plot(x, exacta, 'b', label='Exacta')
plt.title('Solucion numerica para el problema de difusion con $\lambda=0.50$')
plt.xlabel('x')
plt.ylabel('u')
plt.legend(loc=1)
plt.xlim([0,1])
plt.ylim(ymin=0)
plt.show()
