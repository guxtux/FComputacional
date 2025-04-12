from manim import *

class funcion_seno(Scene):

    def construct(self):
        cielo = "#C4DDFF"
        azul = "#001D6E"
        rojo = "#B20600"

        self.camera.background_color=cielo
        
        ax = Axes(color=azul,
                  x_range=[-13, 13, PI],
                  y_range=[-1.3, 1.3, 0.5],
                  axis_config={'include_tip': False},
                #   x_length=9,
                #   y_length=3,
                #   axis_config={'tip_shape': StealthTip},
                  #x_axis_config={"numbers_to_include": [3.14, 6.28, 9.42,12.56]}
                  )
        ax.set_color(azul)

        self.add(ax)
        # self.add_x_labels()
        
    # def add_x_labels(self):
        x_labels = [
            MathTex(r'-3 \pi', color=azul), MathTex(r'-2 \pi', color=azul), MathTex(r'-\pi', color=azul), MathTex(r'0', color=azul), MathTex(r'\pi', color=azul), MathTex(r'2 \pi', color=azul), MathTex(r'3 \pi', color=azul),
        ]

        for i in range(len(x_labels)):
            x_labels[i].move_to(ax.coords_to_point(PI*(i - 3), -0.25))
            self.add(x_labels[i])

        self.wait(1)

        curva0 = ax.plot(lambda x: np.sin(x), color=rojo, x_range=[-4 * PI, 4 * PI])
        eqn0 = MathTex(r'y = \sin{x}', color=azul).move_to(UP * 3.5 + RIGHT * 4).scale(1)
        self.add(eqn0)
        self.play(Write(curva0), run_time=8)
        
        self.wait(1)
