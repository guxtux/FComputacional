# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 16:39:58 2017

@author: Master Chief
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['text.usetex'] = True

# font_path = 'C:\Windows\Fonts\consola.ttf'
# font_prop = font_manager.FontProperties(fname=font_path, size=10)

# title_font = {'fontname':'Arial', 'size':'16', 'color':'black', 'weight':'normal',
#               'verticalalignment':'bottom'}

def etiquetas():
    plt.xlabel('x')
    plt.ylabel('f(x)')

# Creamos un polinomio a partir de los coeficientes
# polinomio = x^3 -10 x^2 + 5
coeficientes = [1., -10, 0, 5]   

# Creamos un array dimensional
x = np.arange(-4, 11, .02)

#  Evaluamos el polinomio en x mediante polyval.
y = np.polyval(coeficientes, x)

# Calculamos las raices del polinomio
raices = np.roots(coeficientes)

# Evaluamos el polinomio en las raices
s = np.polyval(coeficientes, raices)
print(s)
print(raices)
# Las presentamos en pantalla
print("Las tres raíces son: \n x0 = {0:1.3f},\n x1 = {1:1.3f},\n x2 = {2:1.3f}".format(raices[-1], raices[-2], raices[-3]))

plot1 = plt.figure(1)
plt.plot(x, y,'-', label = 'f(x)')
plt.title('Gráfica de la función f(x)')
plt.grid(True)
etiquetas()

# Dibujamos
plot2 = plt.figure(2)
plt.plot(x, y,'-', label = 'f(x)')
plt.plot(raices, s,'ro', label = 'Raíces del polinomio')
plt.title('Gráfica con las tres raíces del polinomio (se ajustan los ejes)',)
plt.axhline(y=0, ls='dashed', lw=0.7, color='k')
plt.axvline(x=0, ls='dashed', lw=0.7, color='k')
plt.text(-1.5,0.5,'$x_{0}$', fontsize=14)
plt.text(1,0.5,'$x_{1}$', fontsize=14)
plt.text(9,0.5,'$x_{2}$', fontsize=14)
plt.axis([-2,11,-3,6])
# Leyenda
plt.legend(loc=9)

# Mostramos la figura en pantalla
plt.show()
