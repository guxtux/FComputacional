#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 13:40:10 2020

@author: gustavo
"""

def fib(n):
    a, b = 0, 1
    while b < n:
        print (b)
        a, b = b, a + b


def fib2(n):
    resultado = []
    a, b = 0, 1
    while a < n:
        resultado.append(a)
        a, b = b, a + b
    return resultado