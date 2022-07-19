# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 22:05:44 2013

@author: IIFCES
"""

import numpy as np
import matplotlib.pyplot as plt

valores = []
errores = []
i = []
exacta = -5.97566

def funcion(h):
    derivada = (np.sin(2*np.pi*(0.45+h))-np.sin(2*np.pi*0.45))/h
    return derivada
x=0
n = 1e-1
#i.append(n)
print('h \t \t derivada \t error')
while n > 1e-16:
    valores.append(funcion(n))
    errores.append(abs((exacta-valores[x])/exacta))
    i.append(n)    
    n =n/10
    x=x+1
    print('{0:1.1e} \t {1:1.6f} \t {2:1.6e}'.format(i[x-1], valores[x-1], errores[x-1]))
    

#print valores
#print '%e' %(errores)

print (len(i), len(errores))
#plt.axis([1e-15,0,1-15,1e2])
#plt.xscale('log')
i.reverse()
errores.reverse()
plt.yscale('log')
plt.plot(i)
plt.plot(errores)
plt.xlabel('Valor de h = $10^{-n}$')
plt.ylabel('Error relativo')
plt.title('Tendencia del error')
plt.show()