# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 13:46:45 2012

@author: IIFCES
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
    X.append(x)
    Y.append(y)
    while x < xStop:
        h = min(h,xStop - x)
        y = y + run_kut4(F,x,y,h)
        x = x + h
        X.append(x)
        Y.append(y)
    return array(X), array(Y)

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

def F(x,y) :
    rho = 300.0
    volumen=0.001
    area = 0.25
    caloresp = 900
    ctransferencia = 30
    emisividad = 0.8
    ctestefanbol = 5.67e-8
    q=3000
    
    constante1 = area/(rho*caloresp*volumen)
    constante2 = emisividad*ctestefanbol
    
    F = zeros(1)
    #F[0] = y[0]
    F[0] = (1/(rho*caloresp*volumen))*(q-(emisividad*ctestefanbol*area)*(y[0]**4-298**4)-(ctransferencia*area)*(y[0]-298))
    return F

x = 0.0
y = array([25])
xStop = 200.0
h = 1
freq=1

X, Y = integrate(F,x,y,xStop,h)
#printSoln(X,Y,freq)
plt.plot(X,Y)
plt.xlabel("Tiempo [minutos]")
plt.ylabel("Temperatura")
plt.title("Distribucion de temperatura contra tiempo")
l=plt.axhline(y=565.0 ,color='r', linestyle ='--')
plt.annotate('Temperatura limite $565^{\circ}C$', xy=(120, 560), xytext=(120, 450),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
plt.show()