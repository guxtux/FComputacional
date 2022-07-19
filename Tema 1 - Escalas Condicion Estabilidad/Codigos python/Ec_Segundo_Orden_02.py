# -*- coding: utf-8 -*-

print ("Programa para calcular las soluciones")
print ("de una ecuación cuadrática ax²+bx+c")
print ("tomando a=b=1, c=10^(-n), n entero positivo,")
print ("usando dos formas distintas de la chicharronera,")
print ("y para calcular el error relativo entre ambas. \n")

import matplotlib.pyplot as plt
import numpy as np
import math

n = 0
while n <= 0 or n != int(n):
    n=int(input("Escribe el valor de n (con n entero > 0): "))

a = b = 1.
c = 10**(-n)
d = b*b - 4*a*c
print ("a =", a, ", b =", b, ", c = ", c, ", n =", n)
print ("Valor del discriminante d =", d)

x1 = (-b + math.sqrt(d))/(2*a)
x2 = (-b - math.sqrt(d))/(2*a)
x3 = -(2*c)/(b - math.sqrt(d))
x4 = -(2*c)/(b + math.sqrt(d))

errorabs14 = abs(x1 - x4)
errorabs23 = abs(x2 - x3)
errorrel14 = abs((x1 - x4)/x4)*100
errorrel23 = abs((x2 - x3)/x3)*100

print ("x4 =", x4, "\nx1 =", x1, "\nx2 =", x2, "\nx3 =", x3, "\n")
print ("Error abs.1,4 = %.2e\nError abs.2,3 = %.2e \n" %(errorabs14, errorabs23))
print ("Error rel.1,4 = %.2e por ciento \nError rel.2,3 = %.2e por ciento \n" %(errorrel14, errorrel23))

def errorrel(cdominio):
    e=[]
    for c in cdominio:
        d = b*b - 4*a*c
        x2 = (-b - math.sqrt(d))/(2*a)
        x3 = -(2*c)/(b - math.sqrt(d))
        errel = abs((x2 - x3)/x3)*100
        e.append(errel)
    return e

cmax=[1e-1, 1e-10, 1e-12, 1e-14]

plt.figure(1)
for i in range(1, 5):
    plt.subplot(2, 2, i)
    cdominio = np.linspace(0., cmax[i-1], 100)
    plt.plot(cdominio, errorrel(cdominio))
    plt.semilogy()
   

#plt.figure(2)
#for i in range(1,5):
#    plt.subplot(2,2,i)
#    plt.ylim(ymax=1)
#    cdominio=np.linspace(0.,cmax[i-1],500)
#    plt.plot(cdominio,errorrel(cdominio))

plt.show()
