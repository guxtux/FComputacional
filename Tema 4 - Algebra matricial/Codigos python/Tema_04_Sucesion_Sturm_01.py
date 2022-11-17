#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: gustavo
"""

from moduloMatrices import sturmSuc, numLambdas
import numpy as np

d = np.ones(4) * 2.0
c = np.ones(3) * -1.

lambda1 = 0.25
lambda2 = 0.5

p1 = sturmSuc(d, c, lambda1)
p2 = sturmSuc(d, c, lambda2)

print('Sucesión Sturm con {0:}'.format(lambda1))
print(p1)
print('\nNúmero de cambios de signo = {0:}'.format(numLambdas(p1)))
print()
print('Sucesión Sturm con {0:}'.format(lambda2))
print(p2)
print('\nNúmero de cambios de signo = {0:}'.format(numLambdas(p2)))

