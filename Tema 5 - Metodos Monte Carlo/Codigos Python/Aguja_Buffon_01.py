from random import random
from math import cos, pi

def cruza(l=1, d=1):
    
    x = d*random()
    
    y = l*cos(pi/2*random())
    if y > x:
        return True
    else:
        return False

lanzmientos = 10000000
N = 0
C = 0
L = 0.25
D = 0.75
  
while N < lanzmientos:
    N += 1
    if cruza(L, D):
        C+=1

aproximacion_Pi = (2.0*L*N)/(D*C)

print('Agujas que cruzaron la línea = {0:}'.format(C))
print('Número de intentos = {0:}'.format(N))
print()
print('Aproximación del valor de pi calculado = {0:} = '.format(aproximacion_Pi))
print('Error relativo = {0:1.5e}'.format(abs(pi - aproximacion_Pi)/pi))