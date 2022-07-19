# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 15:27:43 2013

@author: IIFCES
"""

import matplotlib.pyplot as plt
from math import *
import numpy as np

t=np.arange(0.,4*pi,0.1)
b=328.33
a=20.33


r=1/np.sqrt((np.sin(t)**2/a)+(np.cos(t)**2/b))
plt.polar(t,r)
plt.show()