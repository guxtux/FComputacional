# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 15:40:31 2017

@author: Master Chief
"""

from scipy import interpolate
from numpy import array as np
import matplotlib.pyplot as plt


x0 = 1.5
x = [1., 2., 3., 4.]
f = [0.671, 0.620, 0.567, 0.512]

y = interpolate.interp1d(x,f, fill_value=x0)

print(y)