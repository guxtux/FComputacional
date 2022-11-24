#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: gustavo
"""

import matplotlib.pyplot as plt

x = []

a, semilla, c, m, n = 128, 10, 0, 509, 500
for i in range (1, n):
   nuevasemilla = (a * semilla + c) % m
   semilla = nuevasemilla
   x.append( nuevasemilla)

y = []

a, semilla, c, m, n = 269, 10, 0, 2048, 500

for i in range (1, n):
   nuevasemilla = (a * semilla + c) % m
   semilla = nuevasemilla
   y.append( nuevasemilla)

plot1 = plt.figure(1)
plt.plot(x, '+r')

plot2 = plt.figure(2)
plt.plot(y, '+b')

plt.show()

