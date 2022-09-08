# -*- coding: utf-8 -*-
"""
Created on Thu Mar 07 13:40:35 2013

@author: IIFCES
"""
import matplotlib.pyplot as plt
import numpy as np
from newtonPoli import coeffts, evalPoli
from prettytable import PrettyTable

def yExacta(x):
    valor = 4.8 * np.cos(np.pi * x/20.0)
    return valor

def etiquetas():
    plt.xlabel('Variable independiente x')
    plt.ylabel('Variable dependiente f (x)')
    plt.title(u'Interpolación con Método de Newton')
    plt.legend(loc='best')

xDatos = np.array([0.15, 2.3, 3.15, 4.85, 6.25, 7.95])
yDatos = np.array([4.79867, 4.49013, 4.2243, 3.47313, 2.66674, 1.51909])
x0 = []
y0 = []
yExa = []
x2 = np.linspace(0, 8)

a = coeffts(xDatos, yDatos)

# tabla = PrettyTable(['x', 'yInterp', 'yExacta'], float_format='1.5')

print('x \t yInterp \t yExacta')
print('-'*30)

for x in np.arange(0.0, 8.1, 0.5):
    y = evalPoli(a, xDatos, x)
    # tabla.add_row([x, y, yExacta(x)])
    print('{0:1.5f} \t {1:1.5f} \t {2:1.5f}'.format(x, y, yExacta(x)))
    x0.append(x)
    y0.append(y)

# print(tabla)
    
plot1 = plt.figure(1)
plt.plot(xDatos, yDatos, '+b', label='Datos iniciales')
etiquetas()

plot2 = plt.figure(2)
plt.plot(xDatos, yDatos, '+b', label='Datos iniciales')
plt.plot(x0, y0, '+r', label='Datos interpolados')
etiquetas()

plot3 = plt.figure(3)
plt.plot(xDatos, yDatos, '+b', label='Datos iniciales')
plt.plot(x0, y0, '+r', label='Datos interpolados')
plt.plot(x2, yExacta(x2), 'k', lw=0.7, ls='dashed', label=u'Función exacta')
etiquetas()

plt.show()
