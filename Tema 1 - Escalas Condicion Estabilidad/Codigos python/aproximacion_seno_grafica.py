# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 19:16:37 2020

@author: gusto
"""
import numpy as np
import matplotlib.pyplot as plt

n = 10
x = np.linspace(-2.*np.pi, 2*np.pi, 50)
valores=[]


for j in x:
    suma = j
    term = j
    for i in range(2, n):
        term = (-term *j*j)/((2*i-1)*(2*i-2))
        suma = suma + term
    valores.append(suma)
    
plt.plot(x, np.sin(x), label='Exacta')
plt.plot(x, valores, 'r+', label='Aproximación')
plt.title('Comparación entre la función exacta y la aproximación')
plt.axhline(y=0, ls='dashed', lw=0.7, color='k')
plt.axis([-2*np.pi, 2*np.pi, -1.1, 1.1])
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol=2)
plt.show()
