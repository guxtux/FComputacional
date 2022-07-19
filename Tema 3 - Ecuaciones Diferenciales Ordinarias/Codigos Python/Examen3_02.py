# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 13:46:45 2012

@author: IIFCES
"""

from numpy import *
import matplotlib.pyplot as plt

X=[]
Y=[]
T=[]
ub=150.0
vb=150.0
h=0.1
t=0.0
x=0.0
y=0.0
c=0.005

for i in range(598):
    t = t+h
    vel1 = sqrt(ub**2+vb**2)
    k1 = -c*vel1*ub*h
    l1=(-9.8-c*vel1*vb)*h
    vel2=sqrt((ub+k1)**2+(vb+l1)**2)
    k2 = -c*vel2*(ub+k1)*h
    l2=(-9.8-c*vel2*(vb+l1))*h
    u=ub+(k1+k2)*h
    v=vb+(l1+l2)*h
    x = x+0.5*(u+ub)*h
    y= y+0.5*(v+vb)+h
    ub=u
    vb=v
    X.append(x)
    Y.append(y)
    T.append(t)

for i in range(len(X)):
    X[i]= X[i]**2
    Y[i]= Y[i]**2
    Resultante = sqrt(X[i] + Y[i])
    print i, Resultante

x=linspace(1,599,599)
print len(x), len(Resultante)
plt.plot(x,Resultante)
#plt.xlabel("Tiempo [minutos]")
#plt.ylabel("Temperatura")
#plt.title("Distribucion de temperatura contra tiempo")
#l=plt.axhline(y=565.0 ,color='r', linestyle ='--')
#plt.annotate('Temperatura limite $565^{\circ}C$', xy=(120, 560), xytext=(120, 450),
#            arrowprops=dict(facecolor='black', shrink=0.05),
#            )
plt.show()