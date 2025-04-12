from manim import *
import numpy as np

class ModuloFuncionCompleja3D(ThreeDScene):
    def construct(self):
        # Activar cámara 3D
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)

        # Crear un plano complejo
        axes = ThreeDAxes(
            x_range=[-4, 4, 1],   # parte real
            y_range=[-4, 4, 1],   # parte imaginaria
            z_range=[0, 20, 5],   # valor de |f(z)|
            x_length=7,
            y_length=7,
            z_length=5,
        )

        # Etiquetas de ejes
        labels = axes.get_axis_labels(x_label="Re(z)", y_label="Im(z)", z_label="|f(z)|")

        # Definir |f(z)| = |z^3 - 2z^2 - 3z + 10|
        def complex_function(u, v):
            z = complex(u, v)
            fz = z**3 - 2*z**2 - 3*z + 10
            return np.abs(fz)

        # Crear la superficie 3D
        surface = Surface(
            lambda u, v: axes.c2p(u, v, complex_function(u, v)),
            u_range=[-3, 3],
            v_range=[-3, 3],
            resolution=(100, 100),
            color=BLUE,
            # opacity=0.8,
            checkerboard_colors=[BLUE_D, BLUE_E]
        )

        # Título opcional
        titulo = MathTex(r"|f(z)| = |z^3 - 2z^2 - 3z + 10|")
        titulo.to_corner(UL)

        # Animar
        self.play(Create(axes), Write(labels))
        self.play(Write(titulo))
        self.play(Create(surface))
        self.wait(2)
        self.move_camera(phi=60 * DEGREES, theta=-45 * DEGREES, run_time=4)
        self.wait(3)
