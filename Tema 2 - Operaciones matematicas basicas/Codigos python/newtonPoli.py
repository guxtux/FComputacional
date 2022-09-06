# -*- coding: utf-8 -*-
"""
Created on Thu Mar 07 13:37:53 2013

@author: Gustavo Contreras Mayén
"""

# módulo newtonPoli

def evalPoli(a,xDatos,x):
    n = len(xDatos) - 1 # Grado del polinomio
    p = a[n]
    for k in range(1,n+1):
        p = a[n-k] + (x -xDatos[n-k])*p
    return p
    
def coeffts(xDatos,yDatos):
    m = len(xDatos) # Número de puntos
    a = yDatos.copy()
    for k in range(1,m):
        a[k:m] = (a[k:m] - a[k-1])/(xDatos[k:m] - xDatos[k-1])
    return a