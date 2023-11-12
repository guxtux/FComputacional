# -*- coding: utf-8 -*-
"""

@author: gusto
"""

import numpy as np
import matplotlib.pyplot as plt

# Esta función es la misma que eulerPC pero se hace un ajuste en los tamaños de 
# las listas, así como en la secuencia de enteros de range. Revisa las diferencias
# con respecto a la funcion eulerPC. La función debe de estar en el módulo MetodosDirectos
def eulerPC2(t, ht, y, n, Func):

    f1 = [0] * (n+1); f2 = [0] * (n+1)
    yt = [0] * (n+1)
 
    # Lado derecho de la EDO en t
    Func(t, y, f1)

    # Paso predictor
    for i in range(1, n+1): yt[i] = y[i] + ht * f1[i]
    
    # Lado derecho de la EDO en t+ht
    Func(t + ht, yt, f2)
 
    ht2 = ht/2e0

    # Paso corrector
    for i in range(1, n+1): y[i] += ht2 * (f1[i] + f2[i])
    
    return y

  
def Func(t, y, f):
   f[1] = y[3]
   f[2] = y[4]
   f[3] = -k/m * y[3]*np.fabs(y[3])
   f[4] = -k/m * y[4]*np.fabs(y[4]) - g

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
Cd = 0.e0
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

y[1] = x0 
y[2] = y0
y[3] = vx0
y[4] = vy0

tt[1] = t
xt[1] = y[1]
yt[1] = y[2]


# ---- Solución con el método Predictor-Corrector de Euler ----

while (t + ht <= tmax):
    eulerPC2(t, ht, y, n, Func)
    t += ht
    it += 1
   
    tt[it] = t
    xt[it] = y[1]
    yt[it] = y[2]
   
    if (y[2] < 0.e0): break

print('Método de Euler Predictor-Corrector con CD = 0')
print('\nxmax = {0:5.2f} m'.format(y[1]))

hmax = np.argmax(yt)

print('hmax = {0:3.2f} m'.format(yt[hmax]))

# El contador it nos dice el índice en el cual se alcanza el desplazamiento máximo
# pero el tamaño del objeto es mayor, si graficamos todo el objeto, veremos que la línea
# se "regresa" al origen, por lo debemos de omitir esos valores que son ceros.

plot1 = plt.figure(1)
plt.plot(xt[:it], yt[:it])
plt.plot(y[1], 0, 'ok')
plt.title(r'Distancia máxima alcanzada en el lanzamiento con $C_{D}= 0$ - Euler PC')
plt.xlabel('x')
plt.ylabel('y')
plt.text(50, 5, r'xmax = {0:5.2f} m'.format(y[1]), fontsize=14)
plt.xlim([0, 90])
plt.axhline(y=0, ls='dashed', lw=0.7, color='k')

plt.show()
