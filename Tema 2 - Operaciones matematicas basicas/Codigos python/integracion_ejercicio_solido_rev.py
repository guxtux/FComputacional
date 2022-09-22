# -*- coding: utf-8 -*-
"""
Created on Thu Apr 04 19:26:04 2013

@author: gustavo
"""

from moduloIntegracion import trapecios
import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['text.usetex'] = True

def f(x):
    return np.pi * (1 + (x/2)**2)**2
   
def etiquetas():
    plt.xlim([0, 2])
    plt.ylim([0, 13])
    plt.xlabel(r'$x$')
    plt.ylabel(r'$f (x)$')

paneles = [2, 4, 8, 16, 32, 64, 128]
lista2 = []

# print ('{:^3} \t {:^8} \t {:^11} \t {:^18} '.format('i', 'h', 'Integral', 'Error' ))
# print ('{}'.format("-"*55))

for n in paneles:
    lista1= []
    h = 2./n
    #print ('{:=3} \t {:01.5f} \t {:01.9f} \t {:01.8e}'.format(i, h, trapecios(funcion(i),0,2,i),(abs(11.7286-trapecios(funcion(i),0,2,i)))/11.7286))
    lista1.append(n)
    lista1.append(h)
    lista1.append(trapecios(f, 0, 2, n))
    lista1.append(abs(11.7286 - trapecios(f, 0, 2, n))/11.7286)
    lista2.append(lista1)
    
cabeceras = ['n', 'h', 'Integral', 'Error rel']

print(tabulate(lista2, headers = cabeceras, tablefmt="grid", stralign="center", floatfmt=("", "1.5f", "2.9f", "1.8e")))
    
x1 = np.linspace(0, 2, 100)
muestras = 16
xi = np.linspace(0, 2, muestras)
fi = f(xi)
muestraslinea = muestras * 10 + 1
xk = np.linspace(0, 2, muestraslinea)
fk = f(xk)

plot1 = plt.figure(1)
plt.plot(x1, f(x1), 'r')
plt.title('Función del sólido de revolución')
etiquetas()

plot2 = plt.figure(2)
plt.plot(xk, fk, 'r')
plt.plot(xi, fi, marker='o', color='r')
plt.title(r'Área debajo de la curva con $n = 16$')
plt.fill_between(xi, 0, fi, color='g')
for i in range(0, muestras, 1):
    plt.axvline(xi[i], color='w', lw=0.7)
etiquetas()


plt.show()





    
