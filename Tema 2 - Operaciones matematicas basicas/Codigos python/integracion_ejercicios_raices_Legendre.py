# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 12:40:26 2022

@author: gusto
"""

from scipy.special import roots_legendre, eval_legendre
roots, weights = roots_legendre(6)

print(roots)
print(weights)

print(eval_legendre(6, roots))