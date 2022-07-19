# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 17:21:04 2012

@author: M. en C. Gustavo Contreras Mayén.
"""

from numpy import *
import matplotlib.pyplot as plt

def integrate(F,x,y,xStop,h):
    def run_kut4(F,x,y,h):
        # Computes increment of y from Eqs. (7.10)
        K0 = h*F(x,y)
        K1 = h*F(x + h/2.0, y + K0/2.0)
        K2 = h*F(x + h/2.0, y + K1/2.0)
        K3 = h*F(x + h, y + K2)
        return (K0 + 2.0*K1 + 2.0*K2 + K3)/6.0
    X = []
    Y = []
    Total = []
    X.append(x)
    Y.append(y)
    while x < xStop:
        h = min(h,xStop - x)
        y = y + run_kut4(F,x,y,h)
        x = x + h
        X.append(x)
        Y.append(y)
        Total.append(y)
    return array(X), array(Y), array(Total)

def printSoln(X,Y,freq):
    def printHead(n):
        print '\n x ',
        for i in range (n):
            print ' y[',i,'] ',
        print
    
    def printLine(x,y,n):
        print '%13.4e' %x,
        for i in range (n):
            print '%13.4e' %y[i],
        print
    m = len(Y)

    try: n = len(Y[0])
    except TypeError: n = 1
    if freq == 0: freq = m
    printHead(n)
    for i in range(0,m,freq):
        printLine(X[i],Y[i],n)
    if i != m - 1: printLine(X[m - 1],Y[m - 1],n)

def F(x,y): 
    k = 60.
    Q = 50.
    sigma = 5.67e-8
    Area = 1e-4
    P = 0.01
    
    F = zeros(2)
    F[0] = y[1]
    F[1] = (P*sigma)/(Area*k)*(y[1] - 273) - (Q/(k*Area))
    return F

x = 0.0
#la segunda condición exacta queda en 4167
y = array([273,3500])
xStop = 1.0
h = 0.1
freq=1

X, Y, T = integrate(F,x,y,xStop,h)
printSoln(X,Y,freq)
plt.plot(X,Y[:,0])
plt.xlabel("Distancia [m]")
plt.ylabel("Temperatura")
plt.title("Para $y_{2}=3500$ no se cumple la solucion real")
l=plt.axhline(y=273.0 ,color='k', linestyle ='--')
plt.show()
