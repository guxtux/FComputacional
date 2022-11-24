#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: gustavo
"""

import random
import numpy as np 
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Arial'
  
n = 1000000
  
x = np.zeros(n) 
y = np.zeros(n) 
  
for i in range(1, n): 
    val = random.randint(1, 4) 
    if val == 1: 
        x[i] = x[i - 1] + 1
        y[i] = y[i - 1] 
    elif val == 2: 
        x[i] = x[i - 1] - 1
        y[i] = y[i - 1] 
    elif val == 3: 
        x[i] = x[i - 1] 
        y[i] = y[i - 1] + 1
    else: 
        x[i] = x[i - 1] 
        y[i] = y[i - 1] - 1
      
  
plt.plot(x, y)
plt.title('Caminata aleatoria n = {0:} pasos'.format(str(n)))
plt.savefig('plot_caminata_aleatoria_06.eps', format='eps')
plt.savefig('plot_caminata_aleatoria_06.png', format='png')
# plt.savefig("rand_walk"+str(n)+".png",bbox_inches="tight",dpi=600) 
plt.show() 

