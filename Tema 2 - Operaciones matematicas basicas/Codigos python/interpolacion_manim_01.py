from manim import *

class InterpolacionLineal(Scene):
    def construct(self):
        # Definimos los dos puntos entre los que interpolaremos
        punto_inicio = LEFT * 4
        punto_fin = RIGHT * 4

        # Creamos los puntos visuales
        punto_A = Dot(punto_inicio, color=BLUE)
        punto_B = Dot(punto_fin, color=RED)
        self.play(FadeIn(punto_A, punto_B))

        # Etiquetas
        etiqueta_A = Text("A", font_size=24).next_to(punto_A, DOWN)
        etiqueta_B = Text("B", font_size=24).next_to(punto_B, DOWN)
        self.play(Write(etiqueta_A), Write(etiqueta_B))

        # Creamos el punto que se va a mover (interpolación)
        punto_movil = Dot(color=YELLOW)
        punto_movil.move_to(punto_inicio)
        self.play(FadeIn(punto_movil))

        # Animamos la interpolación lineal
        self.play(
            punto_movil.animate.move_to(punto_fin),
            run_time=3,
            rate_func=linear  # interpolación lineal
        )

        self.wait(1)
