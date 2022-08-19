# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
from math import sqrt, cos, sin
import numpy as np

mpl.rcParams['text.usetex'] = True


def cycloid(r):
  x = [] #create the list of x coordinates
  y = [] #create the list of y coordinats
  for theta in np.linspace(0, 2*np.pi, 1000): #loop over a list of theta, which ranges from -2π to 2π
    x.append(r*(theta - sin(theta))) #add the corresponding expression of x to the x list
    y.append(r*(1 - cos(theta))) #same for y
  plt.title('Gráfica de la cicloide')
  plt.xlim([0, 2*np.pi*r])
  plt.plot(x, y, color='r')  #plot using matplotlib.piplot
  tick_pos = [0, np.pi, 2*np.pi, 3*np.pi, 4*np.pi, 5*np.pi, 6*np.pi]
  labels = ['0', '$\pi$', '$2 \pi$', '$3 \pi$', '$4 \pi$', '$5 \pi$', '$6 \pi$']
  plt.xticks(tick_pos, labels)
  plt.grid(True)
  plt.show()  #show the plot


cycloid(3) #call the function