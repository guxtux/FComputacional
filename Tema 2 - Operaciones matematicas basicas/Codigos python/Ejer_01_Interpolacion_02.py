# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 19:54:28 2020

@author: gusto
"""
import numpy as np
import matplotlib.pyplot as plt

def funcion(x):
    return x*np.sin(x)

def metLagrange(n, x0, f):
    calculo=[]
    for k in x0:
        yres = 0
        for i in range(0,n+1):
            z = 1.0
            for j in range(0,n+1):
                if i != j:
                    z = z * (k-x[j])/(x[i]-x[j])
            yres = yres + z*f[i]
        calculo.append(yres)  
    return calculo

n = 4
x0 = np.linspace(0.,np.pi/2, 20)
x = np.linspace(0.,np.pi/2, 5)

print(x)

valory = metLagrange(n, x, funcion(x))

plt.plot(x, valory, 'r+', label='Polinomio')
plt.plot(x0, funcion(x0), label='Exacta')
plt.legend(loc='best')
plt.title('Comparación entre la la función exacta y la interpolación')
plt.show()

