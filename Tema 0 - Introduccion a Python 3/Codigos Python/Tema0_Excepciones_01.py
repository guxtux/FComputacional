# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

while True:
    try:
        x = int(input("Por favor ingrese un número: "))
        break
    except ValueError:
        print("Oops! No era válido. Intente nuevamente...")