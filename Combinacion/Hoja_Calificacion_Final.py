# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Frame
from reportlab.lib.enums import TA_LEFT, TA_JUSTIFY
import csv
from numpy import array
import os


def concatenaNombre(nombres, apellido1, apellido2):
    return nombres + " " + apellido1 + " " + apellido2

def defineSaludo(entrada):
    if entrada == "1":
        return "Alumno"
    else:
        return "Alumna"

def elaboraConstancia(nombreCompleto, numeroCuenta, examenParcial01, examenTema03, examenTema04, examenTema05, promedioExamenes, promedioEjercicios, calificacionFinal):
    ruta = '2023_1_Cartas/'
    nombre_archivo = nombreCompleto.strip() + '_Resumen_Evaluaciones_Fisica_Computacional.pdf'
    outfilepath = os.path.join( ruta, nombre_archivo )
    objetoCanvas = Canvas(outfilepath, pagesize=letter)
    
    objetoCanvas.drawString(275, 700, 'Ciudad Universitaria a 5 de diciembre de 2022.')
    
    #Estilo de la hoja.
    
    styles=getSampleStyleSheet()
    
    story1= []
    
    ptextoencabezado = nombreCompleto + '. <br/>'\
                        'Número de cuenta: ' + numeroCuenta
    styles.add(ParagraphStyle(name='Izquierda', alignment=TA_LEFT, fontSize = 14, leading = 20))
    story1.append(Paragraph(ptextoencabezado, styles['Izquierda']))
    
    frame = Frame(50, 600, 6.5*inch, 1*inch, showBoundary=0)
    frame.addFromList(story1, objetoCanvas)
    
    story2 = []
    
    ptextomensaje = 'A continuación se presenta el resumen de la evaluación para el curso de Física ' +\
                    'Computacional que cursaste durante el semestre 2023-1.  <br/><br/>' +\
                    'Exámenes: <br/>' +\
                    'Examen Parcial 1: ' + examenParcial01 + '.<br/>' +\
                    'Examen Tema 3: ' + examenTema03 + '.<br/>' +\
                    'Examen Tema 4: ' + examenTema04 + '.<br/>' +\
                    'Examen Tema 5: ' + examenTema05 + '.<br/>' +\
                    'Promedio Exámenes: ' + promedioExamenes + '.<br/><br/>' +\
                    'En total son 44 ejercicios a cuenta y de clase: <br/>' +\
                    'Promedio Ejercicios: ' + promedioEjercicios + '<br/><br/>' +\
                    'Se te informa que el día martes 6 de diciembre en el laboratorio de cómputo y en la hora ' +\
                    'de clase, se revisará tu situación, por lo que te pedimos amablamente asistas y te enteres ' +\
                    'de lo conducente.<br/><br/>' +\
                    'Te comentamos que al inicio del semestre 2023-1 se mencionaron las reglas para la presentación del ' +\
                    'examen final.<br/><br/>'
                    #                 'Esta calificación se asentará en el acta oficial del curso, una vez que se haya realizado la captura y ' +\
    #                 'y la firma electrónica, se les notificará vía correo electrónico, por lo que en un par de días ' +\
    #                 'ya podrán ver reflejada la calificación en su historial académico. <br/<br/>'
    
    # if calificacionFinal != '5':
    #     ptextomensaje = ptextomensaje + 'Te deseamos el mayor de los éxitos y confiamos en que continues con el mismo esfuerzo ' +\
    #                     'y compromiso en lo que resta de la carrera de Física.<br/><br/>M. en C. Ramón Gustavo Contreras Mayén.'
    # else:
    ptextomensaje = ptextomensaje + '<br/><br/>Atentamente,<br/>M. en C. Ramón Gustavo Contreras Mayén.'
            
                    
                    
    styles.add(ParagraphStyle(name='Justificado', alignment=TA_JUSTIFY, fontSize = 12, leading = 18))
    story2.append(Paragraph(ptextomensaje, styles['Justificado']))
    
    #Definimos otro frame.
    frame2 = Frame(50, 50, 6.5*inch, 7.5*inch, showBoundary=0)
    frame2.addFromList(story2, objetoCanvas)
    
    
    objetoCanvas.showPage()
    
    #Salvamos el PDF.
    objetoCanvas.save()

def readinputdata(filename): 
    fichero=open(filename,'r') 
    f=[] 
    line='0' 
    with open(filename) as csv_file:
        for line in csv.reader(csv_file, delimiter=','): #
            if len(line)>0 : 
                f.append(line) 
    fichero.close() 
    return array(f)


data=readinputdata(r'Grupo_2023_1.csv') 
# print (range(1, len(data))) #range(1,26)

for i in range(1, len(data)):
# for i in range(1, 2):
    nombreCompleto = concatenaNombre(data[i][2], data[i][0], data[i][1])
    numeroCuenta = data[i][3]
    print(nombreCompleto)
    examenParcial01 = data[i][4]
    examenTema03 = data[i][5]
    examenTema04 = data[i][6]
    examenTema05 = data[i][7]
    promedioExamenes = data[i][8]
    promedioEjercicios = data[i][9]
    calificacionFinal = data[i][12]
    # bandera = data[i][13]
    # saludo = defineSaludo(data[i][5])
    # ejerciciosEntregados = data[i][26]
    # puntajeObtenido = data[i][28]
    # promedioCalculado = data[i][29]
    # ajustePromedio = data[i][30]
    # calificacionFinal = data[i][31]
    # calificacionLetra = data[i][32]
    elaboraConstancia(nombreCompleto, numeroCuenta, examenParcial01, examenTema03, examenTema04, examenTema05, promedioExamenes, promedioEjercicios, calificacionFinal)
