# -*- coding: utf-8 -*-
"""
Created on Tue Sep 03 16:42:49 2013

@author: IIFCES
"""

import matplotlib.pyplot as plt
from math import sqrt


t = []
v = []
v2 = []

dt, potencia, masa, tmax = 1, 400, 70, 400
#potencia = 400
#masa = 70
#tmax = 400
nmax = tmax/dt
A, C = 0.33, 0.5
#C = 0.5


t.append(0)
v.append(4)
v2.append(4)

for i in range(int(nmax)):
    ti = t[i] + dt
    vi = sqrt(v[i]**2 + (2 * potencia * dt)/masa)
    vc = v2[i-1] + potencia * dt / (masa * v2[i-1]) - (C*A*v2[i-1]**2)*dt/masa
    
    t.append(ti)
    v.append(vi)
    v2.append(vc)
    

plt.plot(v, "r-", label="Sin fricción")
#plt.plot(v, "r-")
plt.plot(v2, "b-", label="Con fricción")
plt.legend(loc="upper left")
plt.xlabel("tiempo [s]")
plt.ylabel("velocidad m/s")
plt.title("Comparación de la velocidad del ciclista")
#plt.title("Velocidad del ciclista sin fricción")
plt.axis([0, 210, 0, 50])
plt.show()
    