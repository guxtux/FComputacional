# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 19:59:26 2023

@author: gusto
"""

import numpy as np
import matplotlib.pyplot as plt


def neville(xDatos, yDatos, x):
    m = len(xDatos)
    y = yDatos.copy()
    for k in range(1,m):
        y[0:m-k] = ((x - xDatos[k:m])*y[0:m-k] +      \
                    (xDatos[0:m-k] - x)*y[1:m-k+1])/  \
                    (xDatos[0:m-k] - xDatos[k:m])
    return y[0]

x0 = np.array([4.0, 3.9, 3.8, 3.7])
y0 = np.array([-0.06604, -0.02724, 0.01282, 0.05382])

x = neville()

plt.plot(x0, y0, 'b+')
plt.plot(x0, y0, 'r--', lw=0.6)
plt.plot(x, 0, 'ro')
plt.xlabel('Valores de x')
plt.ylabel('Valores de y')
plt.title('Gráfica de interpolación con la técnica de Neville')
plt.axhline(y=0, lw=0.7, ls='dashed', color='k')
plt.text(3.85, 0.01, 'y(' + str(round(x,3)) + ') = 0')
plt.show()
