from manim import *

class InterpolacionMultiple(Scene):
    def construct(self):
        # Lista de posiciones por las que pasará el punto
        puntos = [
            LEFT * 5 + DOWN * 2,
            LEFT * 2 + UP * 2,
            RIGHT * 2 + UP * 1,
            RIGHT * 5 + DOWN * 2
        ]

        # Crear y mostrar los puntos como referencia
        puntos_visuales = [Dot(pos, color=BLUE) for pos in puntos]
        etiquetas = [
            Text(f"P{i}", font_size=24).next_to(p, DOWN)
            for i, p in enumerate(puntos_visuales)
        ]

        for p, e in zip(puntos_visuales, etiquetas):
            self.play(FadeIn(p), Write(e), run_time=0.5)

        # Línea quebrada que une los puntos
        trayectoria = VMobject(color=GREY)
        trayectoria.set_points_as_corners(puntos)
        self.play(Create(trayectoria))

        # Punto móvil que recorre la trayectoria
        punto_movil = Dot(puntos[0], color=YELLOW)
        self.play(FadeIn(punto_movil))

        # Animación de interpolación lineal entre los puntos
        for i in range(1, len(puntos)):
            self.play(
                punto_movil.animate.move_to(puntos[i]),
                run_time=2,
                rate_func=linear
            )

        self.wait(1)
