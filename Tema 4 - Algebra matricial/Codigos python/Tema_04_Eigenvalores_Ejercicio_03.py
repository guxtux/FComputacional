#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: gustavo
"""
from moduloMatrices import lamRango
import numpy as np

d = np.ones(3) * 4
c = np.ones(2) * (-2.0)

d[-1] = 5

x = lamRango(d, c, 3)

print(x)

