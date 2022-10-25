from metodosDirectos import integraorden4
from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['text.usetex'] = True

def interpLineal(f, x1, x2):
    f1 = f(x1)
    f2 = f(x2)

    return x2 - f2 * (x2 - x1) / (f2 - f1)

def condIni(u):
    return np.array([0.0, u])

def r(u):
    X, Y = integraorden4(F, xInicio, condIni(u), xAlto, h)
    y = Y[len(Y) - 1]
    r = y[0] - 1.0
    
    return r

def F(x, y):
    F = np.zeros(2)
    F[0] = y[1]
    F[1] = -3.0 * y[0] * y[1]
    
    return F

def etiquetas(orden):
    plt.axis([0, 2, 0, 1.2])
    plt.axhline(y=1, lw=0.7, ls='dashed', color='k')
    #get handles and labels
    handles, labels = plt.gca().get_legend_handles_labels()
    #specify order of items in legend
    order = orden
    #add legend to plot
    plt.legend([handles[idx] for idx in order],[labels[idx] for idx in order]) 

xInicio = 0.0
xAlto = 2.0
h = 0.1

# Primer intento de CI desconocida
u1 = 1.0
X1, Y1 = integraorden4(F, xInicio,condIni(u1), xAlto, h)

# Primer intento de CI desconocida
u2 = 2.0
X2, Y2 = integraorden4(F, xInicio,condIni(u2), xAlto, h)

# Valor de CI interpolada
u = optimize.ridder(r, u1, u2)
X3, Y3 = integraorden4(F, xInicio,condIni(u), xAlto, h)

plot1 = plt.figure(1)
plt.plot(X1, Y1[:,0], 'r', label=r'$u_1$ = {0:}'.format(u1))
plt.plot(X2, Y2[:,0], 'b', label=r'$u_2$ = {0:}'.format(u2))
plt.title('Solución con los valores de CI de prueba')
plt.legend(loc='best')
etiquetas([1,0])
# plt.savefig('plot_Ejercicio_01_Metodo_Disparo_01.eps', format='eps')
# plt.savefig('plot_Ejercicio_01_Metodo_Disparo_01.png', format='png')

plot2 = plt.figure(2)
plt.plot(X3, Y3[:,0], 'm', label=r'$u = {0:1.2f}$'.format(u))
plt.plot(X1, Y1[:,0], 'r', label=r'$u_1$ = {0:}'.format(u1))
plt.plot(X2, Y2[:,0], 'b', label=r'$u_2$ = {0:}'.format(u2))
plt.title(r'Solución con los valores de CI de prueba y el valor de CI interpolado $u$')
etiquetas([2, 0, 1])
# plt.savefig('plot_Ejercicio_01_Metodo_Disparo_02.eps', format='eps')
# plt.savefig('plot_Ejercicio_01_Metodo_Disparo_02.png', format='png')

plt.show()



