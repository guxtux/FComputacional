#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 17:50:09 2020

@author: gustavo
"""

import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(0,18, 200)
x2 = np.linspace(0, 5, 100)

plt.figure(1)                
plt.subplots_adjust(hspace=0.5)

plt.subplot(211)        
plt.plot([1, 2, 3])
plt.title('Ventana 1 - Subplot 1')

plt.subplot(212)         
plt.plot(x1, np.cos(x1))
plt.title('Ventana 1 - Subplot 2')

plt.figure(2)                
plt.plot(x2, np.exp(x2), 'r')           
plt.title('Ventana 2')

plt.show()