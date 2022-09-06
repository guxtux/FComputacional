# -*- coding: utf-8 -*-
# """
# Created on Tue Mar 10 19:51:36 2020

# @author: gusto
# """

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

mpl.rcParams['text.usetex'] = True

def etiquetas():
    plt.title('Ejercicio de interpolación')
    plt.xlabel('Variable independiente x')
    plt.ylabel('Variable dependiente P(x)')

n = 3
x0 = np.array([1.5, 2.5, 3.5])
x = np.array([1., 2., 3., 4.])
f = np.array([0.671, 0.620, 0.567, 0.512])

x1 = np.linspace(1, 4)


datos = []

for k in x0:
    yres = 0
    for i in range(0, n + 1):
        z = 1.0
        for j in range(0, n + 1):
            if i != j:
                z = z * (k - x[j])/(x[i] - x[j])
        yres = yres + z*f[i]
    
    datos.append(yres)
    print ('El polinomio evaluado en P(',k,') =',  yres)

poli_x = np.concatenate([x, x0])
poli_y = np.concatenate([f, datos])

interp_1 = interpolate.interp1d(poli_x, poli_y, kind='cubic')
y1 = interp_1(x1)

plot1 = plt.figure(1)
plt.plot(x, f, '+r', label='Experimentales')
etiquetas()
#plt.savefig('Ejercicio_Interpolacion_01.eps', format='eps')

plot2 = plt.figure(2)
plt.plot(x, f, '+r', label='Experimentales')
plt.plot(x0, datos, 'ob', label= 'Interpolados')
plt.legend(loc='best')
etiquetas()
#plt.savefig('Ejercicio_Interpolacion_02.eps', format='eps')

plot3 = plt.figure(3)
plt.plot(x, f, '+r', label='Experimentales')
plt.plot(x0, datos, 'ob', label= 'Interpolados')
plt.plot(x1, y1, 'm', label='Polinomio interp.')
plt.legend(loc='best')
etiquetas()

plt.show()