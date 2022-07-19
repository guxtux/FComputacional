# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 16:08:51 2013

@author: IIFCES
"""

import matplotlib.pyplot as plt
import numpy as np

# Método de Horner
def P_Horner(x):                         
    P_Hor = 0
    for n in range(len(a)-1, -1, -1):     
        P_Hor = a[n] + P_Hor * x
    return P_Hor

# Método directo
def P_Directo(x):
    return 2 + 4 * x - 5 * x**2 + 2 * x**3 - 6 * x**4 + \
            8 * x**5 + 10 * x**6

# Cálculo de error relativo
def Err_Rel(p, p_): return np.fabs(p - p_)/p*100


# Valores de x0 para evaluar P(x0)
x0 = [-1.5, -0.65, 0.1, 1.4, 2.87]

# Coeficientes a de P(x)
a = [2, 4, -5, 2, -6, 8, 10]

# intervalo
x1 = np.linspace(-2, 3, 50)

# Grafica

plt.plot(x1, P_Horner(x1),'ro', label="Método de Horner")
plt.plot(x1 ,P_Directo(x1), label=u'Evaluación Polinomio')
plt.title(u'Comparación gráfica para un conjunto mayor de puntos')
plt.legend(loc='upper left')
plt.axis([-2, 3, -110, 7000])
plt.grid(True)
plt.show()