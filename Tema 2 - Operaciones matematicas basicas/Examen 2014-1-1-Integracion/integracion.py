# -*- coding: utf-8 -*-

from math import cos, acos
import matplotlib.pyplot as plt
from numpy import linspace

# Metodos de integracion:
#    rectangulos
#    trapecios
#    Simpson 1/3
#    Simpson 3/8


def rectangulos(f,x0,xf,n):
   # Se obtiene la integral numerica de la funcion f, desde el valor 
   # inicial x0 al valor final xf mediante el metodo de rectangulos, 
   # utilizando n+1 datos.
   h = (xf-x0)/n
   x = x0
   suma = 0
   for i in range(n):
      suma += f(x)
      x += h
   return h*suma


def trapecios(f,x0,xf,n):
   # Se obtiene la integral numerica de la funcion f, desde el valor 
   # inicial x0 al valor final xf mediante el metodo de trapecios, utilizando
   # n+1 datos.
   h = (xf-x0)/n
   x = x0
   suma = 0
   for i in range(1,n):
      x +=h
      suma += f(x)
   return (h/2.)*(f(x0) + f(xf) + 2*suma)


def Simpson13(f,x0,xf,n):
   # Se obtiene la integral numerica de la funcion f, desde el valor 
   # inicial x0 al valor final xf mediante el metodo Simpson 1/3, utilizando
   # n+1 datos, donde n debe ser par.
   n = n - n%2 # truncar al numero par mas cercano
   print n
   if n<=0:
      n = 1
   h = (xf-x0)/n
   x = x0
   suma = 0
   for j in range(n/2):
      suma += f(x) + 4.*f(x+h) + f(x+2*h)
      x += 2*h
   return (h/3.)*suma


def Simpson38(f,x0,xf,n):
   # Integracion mediante Simpson 3/8
   n = n - n%3 # truncar al multiplo de 3 mas cercano
   if n<=0:
      n = 1
   h = (xf-x0)/n
   x = x0
   suma = 0
   for j in range(n/3):
      suma += f(x) + 3.*f(x+h) + 3.*f(x+2*h) + f(x+3*h)
      x += 3*h
   return (3.*h/8)*suma


def Romberg(f,x0,xf,Eps=0.01):
   # Se obtiene la integral numerica de la funcion f, desde el
   # valor inicial x0 al valor final xf mediante el metodo de
   # Romberg y trapecios.
   n = 1
   i = 1
   R = [[trapecios(f,x0,xf,n)]]
   while True:
      n *= 2
      i += 1
      R += [[trapecios(f,x0,xf,n)]]
      j = 0
      for k in range(i-1,0,-1):
         j += 1
         R[k-1] += [R[k][j-1]+1./(4**j-1)*(R[k][j-1]-R[k-1][j-1])]
      if abs(R[0][j]-R[1][j-1]) < Eps:
         return R[0][j]

def f(x):
    return cos(2*acos(x))

F = []

print Simpson13(f,-1.,1.,2)
t = linspace(-1.,1.)
for i in t:
   y= f(i)
   F.append(y)


plt.plot(t,F)
l =plt.axhline(y=0.0 ,color='k', linestyle ='-')
s =plt.axvline(x=0.0 ,color='k', linestyle ='-')
plt.show()
