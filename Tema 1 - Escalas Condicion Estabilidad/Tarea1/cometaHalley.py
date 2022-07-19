# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 16:38:10 2013

@author: IIFCES
"""
import matplotlib.pyplot as plt
from math import *

n = 200000
m = 20;
i=0  
t=[]
x=[]
y=[]
r=[]
vx=[]
vy=[]
gx=[]
gy=[]
h = 2.0/(n-1)
h2 = h*h/2
k = 39.478428;


t.append(0.)
x.append(1.966843)
y.append(0)
r.append(x[0])
vx.append(0)
vy.append(0.815795)
gx.append(-k/(r[0]*r[0]))
gy.append(0)

for i in range(0,200000):
#      print h, h*(i+1)
      t.append(h*(i+1))
 #//      x[i+1]  = x[i] + h*vx[i];
      x.append(x[i]+h*vx[i] + h2*gx[i])

#//      y[i+1]  = y[i] + h*vy[i];
      y.append(y[i] + h*vy[i] + h2*gy[i])
      
      r2 = x[i+1]*x[i+1]+y[i+1]*y[i+1]
      
      r.append(sqrt(r2))
      
      r3 = r2*r[i+1]
      gx.append(-k*x[i+1]/r3)
      gy.append(-k*y[i+1]/r3)
#//      vx[i+1] = vx[i] + h*gx[i];
      vx.append(vx[i] + h*gx[i] + k*h2*(3*x[i]*(x[i]*vx[i]+y[i]*vy[i])/(r[i]*r[i])- vx[i])/(r[i]*r[i]*r[i]))
#//    vy[i+1] = vy[i] + h*gy[i];
      vy.append(vy[i] + h*gy[i]+ k*h2*(3*y[i]*(y[i]*vy[i]+x[i]*vx[i])/(r[i]*r[i])- vy[i])/(r[i]*r[i]*r[i]))
#      i=i+1

#for i in range(0,200):
#    print t[i], r[i]
#    i=i+m
 
plt.plot(t,r)
plt.show()