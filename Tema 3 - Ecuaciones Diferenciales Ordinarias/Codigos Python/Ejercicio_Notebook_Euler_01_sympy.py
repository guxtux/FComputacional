#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 10:58:20 2022

@author: gustavo
"""

# %% Symbolic library and its initialization
import sympy as sy
from scipy.special import erfi
import numpy as np
import matplotlib.pyplot as plt

sy.init_printing()

# %% Some common variables
x = sy.symbols('x')

y = sy.Function('y')
y1 = sy.Derivative(y(x), x)

# %% General solution

# Definition
eqdiff = y1 + x * y(x) - 1

# Solution
sol = sy.dsolve(eqdiff, y(x))

# Print
sy.pprint(sol)
# %% Solution with the initial conditions
sol = sy.dsolve(eqdiff, y(x),ics={y(1): '1'})
sy.pprint(sol)

# %% plot using matplotlib
f = sy.lambdify(x, sol.rhs, 'numpy')

x1 = np.linspace(0, 5)

plt.plot(x1, f(x1))

plt.show()