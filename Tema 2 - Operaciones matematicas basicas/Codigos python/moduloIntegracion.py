#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: gustavo
"""

def trapecios(f, a, b, n):
   h = (b - a)/float(n)
   x = a
   suma = f(a)
   
   for i in range(1, n):
      x = x + h
      suma = suma + 2 * f(x)
   
   suma = suma + f(b)
   
   return h * (suma * 0.5)

def simpson13(f, x0, xf, n):
   # n debe ser par
   n = n - n%2
   print (n)
   
   if n<=0:
      n = 1
   
   h = (xf - x0)/n
   x = x0
   suma = 0
   
   for j in range(int(n/2)):
      suma += f(x) + 4. * f(x + h) + f(x + 2 * h)
      x += 2 * h
   return (h/3.) * suma

def simpson38(f, x0, xf, n):
   n = n - n%3 # truncar al multiplo de 3 mas cercano
   
   if n<=0:
      n = 1
   
   h = (xf-x0)/n
   x = x0
   suma = 0
   
   for j in range(n/3):
      suma += f(x) + 3. * f(x + h) + 3. * f(x + 2 * h) + f(x + 3 * h)
      x += 3 * h
   return (3. * h/8) * suma