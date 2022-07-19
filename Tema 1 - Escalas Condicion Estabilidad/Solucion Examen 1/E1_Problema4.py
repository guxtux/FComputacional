 #-*- coding: utf-8 -*-
"""
Created on Wed Feb 27 17:25:40 2013

@author: IIFCES
"""

import matplotlib.pyplot as plt
from math import *
from numpy import ones

def Eabs(x,x_): return abs(x-x_)
def Erel(x,x_): return abs((x-x_)/x)

#Sea s[n]=Sen(theta[n])
s=[0,0,1]
p=[0,0,2]
print "Seno(theta[n]), p[n], Err. Relativo (p[n] con 4Arctan(1))"
for n in range(3,21):
    s.append(s[n-1]/sqrt(2*(1+sqrt(1-(s[n-1])**2))))
    p.append(2**(n-1)*s[n])
    print p[n], '%e' %Erel(p[n],4.0*atan(1.0))

constante = 3.14*ones(21)
plt.axis([1,20,0,3.5])
plt.xlabel('Sectores')
plt.ylabel('Valor de $\pi$')
plt.title('Problema 4 - Calculo de ' + r'$\pi$')
plt.plot(constante)
plt.plot(p, 'go-')
plt.show()