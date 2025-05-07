from manim import *

class funcion_g(Scene):

    def construct(self):
        cielo = "#C4DDFF"
        azul = "#001D6E"
        rojo = "#B20600"

        self.camera.background_color=cielo

        ax = Axes(color=azul,
                  x_range=[-13, 13, PI],
                  y_range=[0, 15, 5],
                  axis_config={'include_tip': False},
                  )
        ax.set_color(azul)
        self.add(ax)

        curva0 = ax.plot(lambda x: 1/(25*x**2), color=rojo, x_range=[-10, 10], stroke_width=5)
        eqn0 = MathTex(r'y = \dfrac{1}{25 x^{2}}', color=azul).move_to([3, 0.5, 0]).scale(1)
        self.add(eqn0)
        self.play(Write(curva0), run_time=5)
        
        self.wait(1)
