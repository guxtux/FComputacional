# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 14:30:16 2013

@author: IIFCES
"""

import matplotlib.pyplot as plt

import numpy as np


x0=np.arange(-4,-0.5,0.5)         # Valores de x0 para evaluar P(x0)
a=[48.,100,70,-20,2]                     # Coeficientes a de P(x)

def P_Horner(x):                         # Método de Horner
    P_Hor=0
    for n in range(len(a)-1,-1,-1):     
        P_Hor=a[n]+P_Hor*x
    return P_Hor

def P_Directo(x):                        # Método directo
    return 48+100*x+70*x**2-20*x**3+2*x**4

def Err_Rel(p,p_): return (p-p_)/p*100   # Cálculo de error relativo

print len(x0)

for i in range(len(x0)):                 # Evaluación de valores de P(x0)
    print "P(%.2f) =" %x0[i],P_Horner(x0[i]), "; Error rel. =", Err_Rel(P_Directo(x0[i]),P_Horner(x0[i]))
    
x=np.linspace(-4.,-1.)                    # Gráfico
plt.plot(x,P_Horner(x),'ro', label=u"Método de Horner")
plt.plot(x,P_Directo(x), label=u'Evaluación Polinomio')
plt.title( u'Problema 3- Comparación grafica')
plt.legend(loc='upper right')
#plt.axis([-2,3,-110,7000])
plt.grid(True)
plt.show()