# import matplotlib as mpl
# import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
from manim import *

class Intro(Scene):

    def construct(self):

        def datos():
            x = np.array([0.0, 1., 2., 2.5, 3.])
            y = np.array([2.9, 3.7, 4.1, 4.4, 5.0])
            return x, y
        
        def minimos_cuadrados(x, y):
            A = np.vstack([x, np.ones(len(x))]).T
            m, c = np.linalg.lstsq(A, y, rcond=None)[0]
            return m, c
        
        def interpolacion(x, y):
            x1 = np.linspace(0, 3)
            f = interp1d(x, y, kind='quadratic')
            return x1, f

        blanco = '#FFFFFF'
        azul = '#001D6E'
        rojo = "#B20600"

        self.camera.background_color=blanco

        ax = Axes(color=azul,
            x_range=[0, 3.5, 0.5],
            y_range=[0, 5, 0.5],
            axis_config={"include_tip": False},
            x_axis_config={'numbers_to_include': np.arange(0, 4.5, 1)},
            y_axis_config={'numbers_to_include': np.arange(0, 5.5, 1)},
        )
        ax.set_color(azul)
                
        x, y = datos()

        p0 = Dot(ax.coords_to_point(x[0], y[0]), color=azul)
        p1 = Dot(ax.coords_to_point(x[1], y[1]), color=azul)
        p2 = Dot(ax.coords_to_point(x[2], y[2]), color=azul)
        p3 = Dot(ax.coords_to_point(x[3], y[3]), color=azul)
        p4 = Dot(ax.coords_to_point(x[4], y[4]), color=azul)

        texto_datos = Tex(r'Datos experimentales', color=azul).scale(0.7).move_to([1.5, 1, 0])
        
        self.add(ax, p0, p1, p2, p3, p4, texto_datos)
        self.wait(1)

        m, c = minimos_cuadrados(x, y)
        recta1 = ax.plot(lambda x: m*x+c, color=rojo, x_range=[0, 3])
        texto_minimos = Tex(r'Mínimos cuadrados', color=rojo).scale(0.7).move_to([1.5, 0, 0])
        self.add(texto_minimos)
        self.play(Write(recta1), run_time=3)
        self.wait(3)

       # Interpolación cuadrática
        f_interp = interp1d(x, y, kind='quadratic')
        x_interp = np.linspace(x[0], x[-1], 100)
        y_interp = f_interp(x_interp)

        # Curva interpolada
        puntos_interp = [ax.coords_to_point(x_interp[i], y_interp[i]) for i in range(len(x_interp))]
        curva = VMobject(color=BLACK)
        curva.set_points_smoothly(puntos_interp)

        texto_interp = Tex(r'Interpolación cuadrática', color=BLACK).scale(0.7).move_to([1.5, -1, 0])
        self.add(texto_interp)
        self.play(Create(curva), run_time=3)
        self.wait(3)

