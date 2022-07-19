# -*- coding: utf-8 -*-

from math import sqrt
print ("Programa para calcular las soluciones")
print ("de una ecuación cuadrática ax²+bx+c")
print ("con coeficientes a,b,c reales,")
print ("usando dos formas distintas de la chicharronera,")
print ("y para calcular el error relativo entre ambas. \n")

a=int(input("Escribe el valor de a: "))
b=int(input("Escribe el valor de b: "))
c=float(input("Escribe el valor de c: "))

d=b*b-4*a*c
print ("a =",a,", b =",b,", c = ",c)
print ("Discriminante d =",d)

x1=(-b+sqrt(d))/(2*a)
x2=(-b-sqrt(d))/(2*a)
x3=-(2*c)/(b-sqrt(d))
x4=-(2*c)/(b+sqrt(d))

errorabs14=abs(x1-x4)
errorabs23=abs(x2-x3)
errorrel14=abs((x1-x4)/x4)*100
errorrel23=abs((x2-x3)/x3)*100

print ("x4 =",x4,"\nx1 =",x1,"\nx2 =",x2,"\nx3 =",x3,"\n")
#print "x4 = %.20f \nx1 = %.20f \nx2 = %.20f\nx3 = %.20f \n" %(x4,x1,x2,x3)
print ("Error abs.1,4 = %.2e\nError abs.2,3 = %.2e \n" %(errorabs14, errorabs23))
print ("Error rel.1,4 = %.2e\nError rel.2,3 = %.2e \n" %(errorrel14, errorrel23))
