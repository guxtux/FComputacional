from manim import *

class polinomio3_01(MovingCameraScene):

    def construct(self):
        # cielo = "#C4DDFF"
        azul = '#001D6E'
        rojo = '#B20600'
        blanco = '#FFFFFF'
        azul_puro = '#0000FF'

        self.camera.background_color=blanco

        ax = Axes(color=azul,
                  x_range=[-3, 4, 1],
                  y_range=[-50, 20, 10],
                  axis_config={'include_tip': False},
                  x_axis_config={'numbers_to_include': np.arange(-3, 4, 1)},
                  y_axis_config={'numbers_to_include': np.arange(-50, 20, 10)},
                  )
        ax.set_color(azul)

        self.add(ax)

        # Se traza la curva y la expresión
        curva0 = ax.plot(lambda x: x**3-3*x**2-x+3, color=rojo, x_range=[-3, 4])
        eqn0 = MathTex(r'f (x) = x^{3} - 3 x^{2} - x + 3', color=azul).to_corner(DR).scale(1)
        self.add(eqn0)
        self.play(Write(curva0), run_time=8)
        
        self.wait(1)

        # Se guarda el estado inicial de la cámara
        self.camera.frame.save_state()

        # Se mueve la cámara para ver la primera raíz
        self.play(
            self.camera.frame.animate.scale(0.5).move_to(np.array([-1, 1, 0]))
        )
        raiz1 = Circle(radius=0.05, color=azul_puro, fill_opacity=1).move_to(ax.c2p(-1, 0))
        x1 = MathTex(r'x_{1}', color=azul).move_to(ax.c2p(-1, 3)).scale(0.75)
        self.add(raiz1, x1)
        self.wait(1)

        # Se mueve la cámara para ver la segunda raíz
        self.play(
            self.camera.frame.animate.scale(1).move_to(np.array([1, 1, 0]))
        )
        raiz2 = Circle(radius=0.05, color=azul_puro, fill_opacity=1).move_to(ax.c2p(1, 0))
        x2 = MathTex(r'x_{2}', color=azul).move_to(ax.c2p(1, 3)).scale(0.75)
        self.add(raiz2, x2)
        self.wait(1)

        # Se mueve la cámara para ver la tercera raíz
        self.play(
            self.camera.frame.animate.scale(1).move_to(np.array([3, 1, 0]))
        )
        raiz3 = Circle(radius=0.05, color=azul_puro, fill_opacity=1).move_to(ax.c2p(3, 0))
        x3 = MathTex(r'x_{3}', color=azul).move_to(ax.c2p(3, 3)).scale(0.75)
        self.add(raiz3, x3)
        self.wait(1)

        # Se mueve la cámara para ver la gráfica completa
        self.play(
            self.camera.frame.animate.scale(2).move_to(np.array([0, 0, 0]))
        )
        self.wait(3)