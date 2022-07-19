# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 22:24:21 2013

@author: IIFCES
"""
from numpy import log, tan,pi,linspace
from scipy import integrate
import matplotlib.pyplot as plt

def recursiva_trapezoid(f,a,b,Ivieja,k):
    if k == 1:Inueva = (f(a) + f(b))*(b - a)/2.0
    else:
            n = 2**(k - 2 ) # Numero de puntos nuevos
            print n
            h = (b - a)/n # Espaciamiento entre los puntos
            x = a + h/2.0 # Coordenada del primer punto  nuevo
            sum = 0.0
            for i in range(n):
                sum = sum + f(x)
                x = x + h
            Inueva = (Ivieja + h*sum)/2.0
    return Inueva

def f(x): return log(1+tan(x))

Ivieja=0.0

for k in range(1,21):
    Inueva= recursiva_trapezoid(f,0.0,pi/4,Ivieja,k)
    if (k>1) and (abs(Inueva - Ivieja)) < 1.0e-06: break
    Ivieja = Inueva

print 'Integral = ' , Inueva
print 'nPaneles = ', 2**(k-1)

print 'Usando scipy =', integrate.quad(f,0.0,pi/4)[0]

x = linspace(0.0,1.0)

plt.plot(x,f(x))
plt.fill_between(x,f(x),0, color='green', alpha=0.25)
plt.axhline(y=0.0, color='k')
plt.axvline(x=2.0, color = 'k', linestyle='--')
plt.title(r'Area debajo de la curva, entre $0$ y $\pi/4$', fontsize=18)
plt.text(0.05,0.75,r'La region verde corresponde a la integral: $\int_{0}^{\pi/4} ln(1 + tan(x))$', fontsize=14)
plt.axis([0,pi/4,0.0,1.0])
plt.xticks([0, pi/16, pi/8, 3*pi/16, pi/4],[r'$0$',r'$\pi/16$',r'$\pi/8$',r'$3\pi/16$', r'$\pi/4$'], fontsize=14)
plt.show()