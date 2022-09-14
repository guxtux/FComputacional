# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 16:39:58 2017

@author: Master Chief
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

font_path = 'C:\Windows\Fonts\consola.ttf'
font_prop = font_manager.FontProperties(fname=font_path, size=10)

title_font = {'fontname':'Arial', 'size':'16', 'color':'black', 'weight':'normal',
              'verticalalignment':'bottom'}

# Creamos un polinomio
polinomio = [1.,-6.4,6.45,20.538,-31.752]   # polinomio = x^4 - 6.4  x^3 + 6.45 x^2 + 20.538 x - 31.752

# Creamos un array dimensional
x = np.arange(-3,5,.02)

#  Evaluamos el polinomio en x mediante polyval.
y = np.polyval(polinomio,x)

# Calculamos las raices del polinomio
raices = np.roots(polinomio)

# Evaluamos el polinomio en las raices
s = np.polyval(polinomio,raices)

print(raices)
print(len(raices))
# Las presentamos en pantalla
for i in range(len(raices)):
    #print ("Las raíces son %2.2f, %2.2f, %2.2f. " % (raices[0], raices[1], raices[2]))
    print ('Las raíces son %2.3f ' %(raices[i]))
    
# Creamos la figura
plt.figure

# Dibujamos
plt.plot(x,y,'-', label = 'f(x)')

# Fibujamos en la figura anterior
#plt.hold('on')

# Dibujamos
plt.plot(raices, s,'ro', label = 'Raíces del polinomio')

# Etiquetas
plt.xlabel('x', fontname='Courier New')
plt.ylabel('f(x)', fontname='Courier New')
plt.title('Raíces del polinomio', **title_font)
plt.axhline(y=0, ls='dashed', lw=0.7, color='k')
plt.axvline(x=0, ls='dashed', lw=0.7, color='k')
#plt.text(-1.5,0.5,'$x_{0}$', fontsize=14)
#plt.text(1,0.5,'$x_{1}$', fontsize=14)
#plt.text(9,0.5,'$x_{2}$', fontsize=14)
plt.axis([-2.5,5,-50,50])
# Leyenda

plt.legend(loc=1, prop=font_prop)

# Mostramos la figura en pantalla
plt.show()