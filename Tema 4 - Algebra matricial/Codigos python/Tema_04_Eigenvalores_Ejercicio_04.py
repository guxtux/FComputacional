#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: gustavo
"""

from moduloMatrices import eigenvalores3
import numpy as np

N = 3
n = 100
d = np.ones(n) * 2.0
c = np.ones(n-1) * (-1.0)

lambdas = eigenvalores3(d, c, N)

print(lambdas)