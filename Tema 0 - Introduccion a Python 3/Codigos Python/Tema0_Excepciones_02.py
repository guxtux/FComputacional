ll#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 11:50:56 2020

@author: gustavo
"""

ocurre_error = False

try:
    numero = float(input('Introduce un numero: '))
    print("La raíz cuadrada del número %f es %f" % (numero, numero ** 0.5))
    
except TypeError as descripcion:
    ocurre_error = True
    print("Ocurrió un error previsto:", descripcion)
    
except:
    ocurre_error = True
    print("¡No sé qué pasó!")
    
if ocurre_error:
    print("Lástima.")
else:
    print("Buen día.")
    