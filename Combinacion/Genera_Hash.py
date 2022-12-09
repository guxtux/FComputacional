#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 13:30:58 2022

@author: gustavo
"""

from Modulo_Funciones import cargaArchivo, generaCadena, quitaEspacios

#-------------------------------------------

archivoInicial = input("Ingresa el nombre del archivo .csv: ")
DF1 = cargaArchivo(archivoInicial)

alumno = []
listaClavesHash256 = []
contador = 0

for i in DF1.index:
    cuenta = str(DF1['Cuenta'][i])
    nombreCompleto = str(DF1['Nombre'][i]) + ' ' + str(DF1['Apellido_1'][i]) + ' ' + \
                    str(DF1['Apellido_2'][i])
    claveHash256 = generaCadena(quitaEspacios(cuenta), quitaEspacios(nombreCompleto))
    alumno.append(nombreCompleto)
    listaClavesHash256.append(claveHash256)
    contador += 1

df2 = DF1.assign(Alumno = alumno, Clave_Hash256 = listaClavesHash256)
df2.drop(columns=['Apellido_1', 'Apellido_2', 'Nombre'], inplace=True)
columnas = ['Alumno', 'Clave_Hash256', 'Cuenta', 'Correo', 'Tarea1', 'Tarea2', 'Tarea3', 'Tarea4', 'Tarea5', 'P_Tareas', 'Ap_Tareas', 'E1', 'E2', 'P_Examen', 'Ap_Examen', 'Promedio', 'Campana', 'Final', 'Comentarios']

df2 =df2[columnas]

df2.to_csv('Lista_2022_2_MAF_8179_Hash256.csv', sep = ',')
print('Se generó el archivo y se procesaron {0:} registros'.format(contador))