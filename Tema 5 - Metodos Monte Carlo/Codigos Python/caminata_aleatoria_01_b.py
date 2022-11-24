#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: gustavo
"""

import numpy as np 
import matplotlib.pyplot as plt 
  
prob = [0.05, 0.95]   
  
inicio = 2  
posiciones = [inicio] 
  
rr = np.random.random(1000)

pabajo = rr < prob[0] 
parriba = rr > prob[1] 
  
  
for ipabajo, iparriba in zip(pabajo, parriba): 
    abajo = ipabajo and posiciones[-1] > 1
    arriba = iparriba and posiciones[-1] < 4
    print(abajo, arriba, posiciones[-1])
      
plt.plot(posiciones)
plt.savefig('plot_caminata_aleatoria_01.eps', format='eps')
plt.savefig('plot_caminata_aleatoria_01.png', format='png')
plt.show() 
