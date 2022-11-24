#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: gustavo
"""

import numpy as np
import matplotlib.pyplot as plt

s = np.random.uniform(-1, 0, 1000)

count, bins, ignored = plt.hist(s, 15, density=True)
plt.plot(bins, np.ones_like(bins), linewidth=2, color='r')
plt.savefig('plot_distribucion_02_uniforme.eps', format='eps')
plt.show()