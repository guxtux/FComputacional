#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 15:37:13 2020

@author: gustavo
"""

from math import pi, trunc #, fabs
#from Modulo_Examen_01 import error_relativo

def truncamiento(numero, digitos) -> float:
    paso = 10.0 ** digitos
    return trunc(paso * numero) / paso

def calcula_pi(k):
    suma = 0
    arreglo = []
    for i in range(k):
        suma = suma + (1/(16 * k**2 - 1))
        arreglo.append(suma)
    print(arreglo)
    


tolerancia = 1
pi10 = truncamiento(pi, 10)
i = 0

#while tolerancia > 1e-08:
#    i += 1
#    v_error = error_relativo(pi10, calcula_pi(i))
#    tolerancia = fabs(pi10/calcula_pi(i))    
#    print(i, calcula_pi(i), v_error)

calcula_pi(3)
calcula_pi(4)
