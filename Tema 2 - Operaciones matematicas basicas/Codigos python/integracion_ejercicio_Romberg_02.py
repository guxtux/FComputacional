#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 18:36:11 2022

@author: gustavo
"""

from numpy import cos, sqrt, pi
from scipy.integrate import romberg

def f(x): return 2.0 * (x**2) * cos(x**2)

resultado = romberg(f, 0, sqrt(pi), show=True)

print(resultado)