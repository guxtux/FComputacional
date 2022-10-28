#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: gustavo
"""

from moduloMatrices import LUdescomp3, LUsoluc3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['text.usetex'] = True

def ecuaciones(x, h, m):
    h2 = h * h
    d = np.ones(m+1) * (-2.0 + 4.0 * h2)
    c = np.ones(m)
    e = np.ones(m)
    b = np.ones(m+1) * 4.0 * h2 * x
    d[0] = 1.0
    e[0] = 0.0
    b[0] = 0.0
    c[m-1] = 2.0
    
    return c, d, e, b

def sol_Exacta(x):
    return x + 0.5 * np.sin(2*x)

def error_rel(aprox):
    valor = ((1.57080 - aprox)/1.57080)
    return valor

def etiquetas():
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(loc=4)
    plt.xlim([0, 1.7])
    plt.axhline(y=0, lw=0.7, ls='dashed', color='k')
    plt.axvline(x=np.pi/2,ymin=0., ymax=.93, ls='dashed', lw=0.7)

xInicio = 0.0
xAlto = np.pi/2.0

# %% Solución con m = 10
m1 = 10


h1 = (xAlto - xInicio)/m1
x = np.arange(xInicio, xAlto + h1, h1)

c, d, e, b = ecuaciones(x, h1, m1)

c, d, e = LUdescomp3(c, d, e)
y = LUsoluc3(c, d, e, b)

print("\n        x              y")

for i in range(m1 + 1):
    print('{:14.5e} {:14.5e}'.format(x[i], y[i]))

x3 = np.linspace(xInicio, xAlto)

# %% Solución con m2 = 100
m2 = 100

h2 = (xAlto - xInicio)/m2
xh2 = np.arange(xInicio, xAlto + h2, h2)

c2, d2, e2, b2 = ecuaciones(xh2, h2, m2)

c2, d2, e2 = LUdescomp3(c2, d2, e2)
y2 = LUsoluc3(c2, d2, e2, b2)

# %% Rutina de graficación con m = 10
cadena = 'La solución con el método de diferencias finitas'
error1 = error_rel(y[-1])
plot1 = plt.figure(1)
plt.plot(x, y, '.b', label='Diferencias finitas')
plt.plot(x3, sol_Exacta(x3), '--r', label='Exacta')
plt.plot(np.pi/2, y[-1], 'bo')
plt.title(cadena.format(m1, y[-1],error1))
plt.text(0.2, 1.25, 'm = 10')
plt.text(0.2, 1.12, r'y (pi/2) = 1.56418')
plt.text(0.2, 1, 'error = 0.4$\%$')
etiquetas()
# plt.savefig('plot_CDF_Dif_Fin_Ejercicio_01_01.eps', format='eps')
# plt.savefig('plot_CDF_Dif_Fin_Ejercicio_01_01.png', format='png')

# %% Rutina de graficación con m = 10
cadena2 = 'La solución con el método de diferencias finitas'
error2 = error_rel(y2[-1])
plot2 = plt.figure(2)
plt.plot(xh2, y2, label='Diferencias finitas')
plt.plot(x3, sol_Exacta(x3), label='Exacta')
plt.plot(np.pi/2, y2[-1], 'bo')
plt.text(0.2, 1.25, 'm = 100')
plt.text(0.2, 1.12, r'y (pi/2) = 1.57073')
plt.text(0.2, 1, 'error =  $\%$')
plt.title(cadena2.format(m2 ,y2[-1], error2))
etiquetas()
# plt.savefig('plot_CDF_Dif_Fin_Ejercicio_01_02.eps', format='eps')
# plt.savefig('plot_CDF_Dif_Fin_Ejercicio_01_02.png', format='png')


plt.show()
