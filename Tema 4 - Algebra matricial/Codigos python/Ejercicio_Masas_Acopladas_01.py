# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 13:00:56 2022

@author: gusto
"""
from moduloMatrices import LUdescomp3, LUsoluc3, eigenvalores3, potenciaInversa3
import numpy as np
from random import random

def inversePower3(d,c,s,tol=1.0e-6):
    n = len(d)
    e = c.copy()
    cc = c.copy()
    dStar = d - s                  # Form [A*] = [A] - s[I]
    LUdescomp3(cc,dStar,e)          # Decompose [A*]
    x = random(n)                    # Seed x with random numbers
    xMag = np.sqrt(np.dot(x,x))  # Normalize [x]
    x = x/xMag
    
    for i in range(30):               # Begin iterations    
        xOld = x.copy()               # Save current [x]
        LUsoluc3(cc,dStar,e,x)        # Solve [A*][x] = [xOld]
        xMag = np.sqrt(np.dot(x,x)) # Normalize [x]
        x = x/xMag
        if np.dot(xOld,x) < 0.0:   # Detect change in sign of [x]
            sign = -1.0
            x = -x
        else: sign = 1.0
        if np.sqrt(np.dot(xOld - x,xOld - x)) < tol:
            return s + sign/xMag,x
    print('Inverse power method did not converge')
    return

k = 500.0e3
m = np.array([1.0, 1.0, 1.0, 8.0, 1.0, 1.0, 8.0])
n = len(m) # Number of masses (DOF)
m = 1.0/np.sqrt(m) # Used in transformation
N = 2 # Number of eigenvalues reqd.
d = np.ones(n)*2.0
d[n-1] = 1.0
c = -np.ones(n-1)
xx = np.zeros((n,N)) # Storage for eigenvectors
# Transform the problem into the standard form
for i in range(n): d[i] = d[i]*m[i]*m[i]
for i in range(n-1): c[i] = c[i]*m[i]*m[i+1]
lam = eigenvalores3(d,c,N) # Compute eigenvalues
# Compute eigenvectors
for i in range(N):
    s = lam[i]*1.0000001 # Shift close to eigenvalue
    eVal,x = potenciaInversa3(d,c,s)
    x = x*m # Eigenvctors of orig. problem
    x = x/np.sqrt(np.dot(x,x)) # Normalize eigenvectors
    xx[:,i] = x # Store in array [xx]
    
# Format and print results
print("Circular frequencies (in rad/s)):")
for i in range(N): print("{:10.6f}".format(np.sqrt(lam[i]*k)),end=" ")
print("\n\nRelative displacements:")

for i in range(n):
    for j in range(N):
        print("{:10.6f}".format(xx[i,j]),end=" ")
    print()