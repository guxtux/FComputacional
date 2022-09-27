#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 21:08:43 2022

@author: gustavo
"""

from scipy.integrate import quadrature

def g(x): return (1 - x**2)**(3/2)

print('La integral vale I = {0:1.8f}'.format(quadrature(g, -1., 1)[0]))