# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 16:08:51 2013

@author: IIFCES
"""

import matplotlib.pyplot as plt
import numpy as np


def P_Horner(x):                         # Método de Horner
    P_Hor = 0
    for n in range(len(a)-1, -1, -1):     
        P_Hor = a[n] + P_Hor * x
    return P_Hor

def P_Directo(x):                        # Método directo
    return 2 + 4 * x - 5 * x**2 + 2 * x**3 - 6 * x**4 + \
            8 * x**5 + 10 * x**6

def Err_Rel(p, p_): return np.fabs(p - p_)/p*100   # Cálculo de error relativo


x0 = [-1.5, -0.65, 0.1, 1.4, 2.87]         # Valores de x0 para evaluar P(x0)
a = [2, 4, -5, 2, -6, 8, 10]                     # Coeficientes a de P(x)
x1 = np.linspace(-2, 3, 50)

arreglo_x = int(len(x0))

for i in range(arreglo_x):                 # Evaluación de valores de P(x0)
    error_rel = Err_Rel(P_Directo(x0[i]), P_Horner(x0[i]))
    print("P({0:.2f}) = {1:.5f} , Error relativo = {2:}".format(x0[i], \
          P_Horner(x0[i]), error_rel))
    if i == 4:
        plt.plot(x0[i], P_Horner(x0[i]),'ro', label="Método de Horner")
    else:
        plt.plot(x0[i], P_Horner(x0[i]), 'ro')

#x=np.linspace(-2.,3.)                    # Gráfico
#
plt.plot(x1 ,P_Directo(x1), label=u'Evaluación Polinomio')
plt.title(u'Comparación gráfica')
plt.legend(loc='upper left')
plt.axis([-2,3,-110,7000])
#plt.grid(True)
plt.show()