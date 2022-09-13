# -*- coding: utf-8 -*-
"""
@author: IIFCES
"""

from math import ceil, log, tan
import numpy as np

def buscaraiz(f, a, b, dx):
    x1 = a; f1 = f(a)
    x2 = a + dx; f2 = f(x2)
    while f1*f2 > 0.0:
        if x1 >= b: return None
        x1 = x2; f1 = f2
        x2 = x1 + dx; f2 = f(x2)
    else:
        return x1, x2

def biseccion(f, x1, x2, switch=0, tol=1.0e-9):
    f1 = f(x1)
    if f1 == 0.0: return x1
    f2 = f(x2)
    if f2 == 0.0: return x2
    
    if f1*f2 > 0.0: print('La raiz no se ha identificado en un intervalo')

    n = ceil(log(abs(x2 - x1)/tol)/log(2.0))
    
    print('x1 \t x3 \t x2 \t f1 \t f3 \t f2')
    print('-'*40)

    for i in np.arange(n):
        x3 = 0.5*(x1 + x2); f3 = f(x3)
        print('{0:1.5f} \t {1:1.5f} \t {2:1.5f} \t {3:1.5f} \t {4:1.5f} \t {5:1.5f}'.format(x1, x3, x2, f1, f3, f2))
        
        if (switch == 1) and (abs(f3) > abs(f1)) \
                        and (abs(f3) > abs(f2)):
            return None
        if f3 == 0.0: return x3
        if f2*f3 < 0.0:
            x1 = x3; f1 = f3
        else:
            x2 =x3; f2 = f3
    return (x1 + x2)/2.0


#Ejercicio 1
def f(x): return x**3 - 10*x**2 + 5.

a = 0.
b = 1.

raiz = biseccion(f, a, b, tol=1.e-4)
print('La raíz en el intervalo ({0:}, {1:}) es: {2:1.4f}'.format(a, b, raiz))



# Ejercicio 2
# def f(x):return x - tan(x)
# a,b,dx = (0., 20.0, 0.01)



# print('Intervalo (x1, x2)   raiz')
# while 1:
#     x1, x2 = buscaraiz(f, a, b, dx)
#     if x1 != None:
#         a = x2
#         raiz = bisect(f,x1,x2,1)
#         if raiz != None: print(x1, x2, raiz)
#     else:
#         print('\nHecho')
#         break
    
# input('Press return to exit')
