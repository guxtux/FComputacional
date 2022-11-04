#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 09:46:59 2022

@author: gustavo
"""

import numpy as np

def ridder(f, a, b, tol=1.0e-9):
    fa = f(a)
    if fa == 0.0: return a
    
    fb = f(b)
    if fa == 0.0: return b
    
    if np.sign(fa) == np.sign(fb): print('La raíz no está en el intervalo')
    #if np.sign(f2)!= np.sign(f3): x1 = x3; f1 = f3
    
    for i in range(30):
        
        # Calcula la raiz x con la formula de Ridder
        c = 0.5 * (a + b); fc = f(c)
        s = np.sqrt(fc**2 - fa * fb)
        
        if s == 0.0: return None
        
        dx = (c - a) * fc/s
        
        if (fa - fb) < 0.0: dx = -dx
        
        x = c + dx; fx = f(x)
      
        # Prueba de convergencia
        if i > 0:
            if np.fabs(x - xOld) < tol*max(np.fabs(x), 1.0): return x
        
        xOld = x
        
        # Vuelva a "encerrar" a la raíz lo más ajustada posible
        if np.sign(fc) == np.sign(fx):
            if np.sign(fa)!= np.sign(fx): b = x; fb = fx
            else: a = x; fa = fx
        else:
            a = c; b = x; fa = fc; fb = fx
            
    return None

    print('Son demasiadas iteraciones')
