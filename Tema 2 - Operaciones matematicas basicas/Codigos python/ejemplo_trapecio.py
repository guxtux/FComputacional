#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 19:38:13 2022

@author: gustavo
"""

from moduloIntegracion import trap

def f(x):
    return x ** 4 * (1 - x) ** 4 / (1 + x ** 2)


print(trap(f, 0, 1, 100))