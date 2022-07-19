# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 16:40:00 2013

@author: IIFCES
"""

from pylab import *
x = arange(10)
y = x*x
ion()
p, = plot(x, y)
for a in arange(0, 10, 0.1):
    x = arange(10) + a
    p.set_xdata(x)
    draw()