#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 12:29:25 2022

@author: gustavo
"""

from moduloDiferencias import dif_adelante_h2, \
                                ddif_adelante_h2, \
                                dif_central_puntos, \
                                ddif_central_puntos, \
                                extra_Richardson

x = [0, 0.1, 0.2, 0.3, 0.4]
fx = [0.0000, 0.0819, 0.1341, 0.1646, 0.1797]

h = 0.1

pderivada = dif_adelante_h2(fx[0], fx[1], fx[2], h)

sderivada = ddif_adelante_h2(fx[0], fx[1], fx[2], fx[3], h)

pderivada2 = dif_central_puntos(fx[1], fx[3], h)
sderivada2 = ddif_central_puntos(fx[1], fx[2], fx[3], h)

print(pderivada)
print(round(sderivada, 4))
print(pderivada2)
print(round(sderivada2, 4))

nueva_derivada1 = dif_adelante_h2(fx[0], fx[2], fx[4], 0.2)
nueva_derivada2 = dif_adelante_h2(fx[0], fx[1], fx[2], 0.1)

print('\n{0:}'.format(nueva_derivada1))
print(nueva_derivada2)

mejora = extra_Richardson(nueva_derivada1, nueva_derivada2, 2)

print('\n{0:}'.format(mejora))