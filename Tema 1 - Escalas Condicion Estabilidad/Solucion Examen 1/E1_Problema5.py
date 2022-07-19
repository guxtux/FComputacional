# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 19:27:36 2013

@author: IIFCES
"""
import matplotlib.pyplot as plt
from math import *

def Eabs(x,x_): return abs(x-x_)
    
def Erel(x,x_): return abs((x-x_)/x)

def Fib1(N):        #Usando relación de recurrencia
    L2=0
    L1=1
    fibonacci=[]
    for n in range(1,N+1):
        fibonacci.append(L1)
        L2,L1=L1,L1+L2
    return fibonacci

def Fib2(N):        #Usando la razón dorada
    fibonacci=[]
    for n in range(1,N+1):
        Ln=(((1.+sqrt(5.))/2)**n-((1.-sqrt(5.))/2)**n)/sqrt(5)
        fibonacci.append(Ln)
    return fibonacci

a=Fib1(50)
b=Fib2(50)
errores = []
print "CÁLCULO DE LA SUCESIÓN DE FIBONACCI MEDIANTE DOS MÉTODOS:"
print "LA RELACIÓN DE RECURRENCIA Y LA RAZÓN DORADA \n"
print " n, Recurrencia,     Razón dorada,       Err.Relativo"
for n in range(0,50):
    errores.append(Erel(a[n],b[n]))
    print "%2d" %(n+1), "%12d" %a[n],"  %20.15f" %b[n], "  %.2e" %Erel(a[n],b[n])

x = range(1,51)
print len(x)
plt.title(u'Problema 5 - Sucesión de Fibonacci')
plt.xlabel(u'Términos de la serie')
plt.ylabel('Error relativo')
plt.plot(errores)
plt.show()