from manim import *
import numpy as np
from scipy.interpolate import interp1d

class InterpolacionCuadratica(Scene):
    def construct(self):
        # Datos
        x = np.array([0.0, 1.0, 2.0, 2.5, 3.0])
        y = np.array([2.9, 3.7, 4.1, 4.4, 5.0])

        # Interpolación cuadrática
        f_interp = interp1d(x, y, kind='quadratic')
        x_interp = np.linspace(x[0], x[-1], 100)
        y_interp = f_interp(x_interp)

        # Ejes
        axes = Axes(
            x_range=[-0.5, 3.5, 0.5],
            y_range=[2.5, 5.5, 0.5],
            axis_config={"include_numbers": True}
        ).add_coordinates()

        self.play(Create(axes))

        # Puntos originales
        puntos = [axes.coords_to_point(x[i], y[i]) for i in range(len(x))]
        dots = VGroup(*[Dot(p, color=RED) for p in puntos])
        labels = VGroup(*[
            Text(f"({x[i]:.1f}, {y[i]:.1f})", font_size=24).next_to(puntos[i], UP)
            for i in range(len(x))
        ])

        self.play(FadeIn(dots), FadeIn(labels))

        # Curva interpolada
        puntos_interp = [axes.coords_to_point(x_interp[i], y_interp[i]) for i in range(len(x_interp))]
        curva = VMobject(color=BLUE)
        curva.set_points_smoothly(puntos_interp)

        self.play(Create(curva), run_time=3)
        self.wait()
