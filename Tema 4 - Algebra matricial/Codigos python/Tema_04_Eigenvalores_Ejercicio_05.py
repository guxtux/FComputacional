#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: gustavo
"""

from moduloMatrices import lamRango, potenciaInversa3
import numpy as np

N = 10
n = 100
d = np.ones(n) * 2.0
c = np.ones(n-1) * (-1.0)
r = lamRango(d, c, N)
s = (r[N-1] + r[N])/2.0
lam, x = potenciaInversa3(d, c, s)

print('Eigenvalor No. {0:} = {1:}'.format(N, lam))