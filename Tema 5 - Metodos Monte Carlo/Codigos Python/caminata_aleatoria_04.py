#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: gustavo
"""

import turtle
from random import randint
from colorsys import hsv_to_rgb

#longitud del paso
paso = 30

#numero de pasos
npasos = 2000

#cambia el valor de matiz de color
hinc = 1.0/npasos

#ancho de la linea
turtle.width(2)

#frontera para la caminata
(w, h) = turtle.screensize()

#velocidad al dibujar
turtle.speed('fastest')

#establece el color del modelo (1:255)
turtle.colormode(1.0)

#pone el fondo de color negro
turtle.bgcolor('black')

#define el matiz
hue = 0.0

for i in range(npasos):
	#proporciona el valor del angulo del paso
    turtle.setheading(randint(0,359))
    
    #cambia el color RGB del lapiz
    turtle.color(hsv_to_rgb(hue, 1.0, 1.0))
    
    #cambia el color
    hue += hinc
    
    #hace un paso hacia adelante
    turtle.forward(paso)
    
    #calcula la posicion de la tortuga
    (x,y) = turtle.pos()
    
    #revisa si esta dentro del cuadro
    if abs(x) > w or abs(y) > h:
    	
    	#si esta por fuera, se regresa
        turtle.backward(paso)
        
turtle.done()

