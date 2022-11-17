#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: gustavo
"""

from moduloMatrices import gerschgorin
import numpy as np

d = np.ones(3) * 4.
c = np.ones(2) * -2.

d[-1] = 5

a, b = gerschgorin(d, c)

print('El intevalo para los eigenvalores es: ({0:}, {1:})'.format(a, b))