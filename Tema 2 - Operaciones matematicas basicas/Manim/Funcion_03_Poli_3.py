from manim import *

class polinomio3_02(MovingCameraScene):

    def construct(self):
        # cielo = "#C4DDFF"
        azul = '#001D6E'
        rojo = '#B20600'
        blanco = '#FFFFFF'
        azul_puro = '#0000FF'

        self.camera.background_color=blanco

        ax = Axes(color=azul,
                  x_range=[-1, 4, 1],
                  y_range=[-30, 10, 10],
                  axis_config={'include_tip': False},
                  x_axis_config={'numbers_to_include': np.arange(-1, 5, 1)},
                  y_axis_config={'numbers_to_include': np.arange(-30, 10, 10)},
                  )
        ax.set_color(azul)

        self.add(ax)

        # Se traza la curva y la expresión
        curva0 = ax.plot(lambda x: x**3-6*x**2+12*x-8, color=rojo, x_range=[-1, 4])
        eqn0 = MathTex(r'f (x) = x^{3} - 6 x^{2} + 12 x - 8', color=azul).to_corner(DR).scale(1)
        self.add(eqn0)
        self.play(Write(curva0), run_time=8)
        
        self.wait(1)

        # Se guarda el estado inicial de la cámara
        self.camera.frame.save_state()

        # Se mueve la cámara para ver la primera raíz
        self.play(
            self.camera.frame.animate.scale(0.5).move_to(np.array([2, 1, 0]))
        )
        raiz1 = Circle(radius=0.05, color=azul_puro, fill_opacity=1).move_to(ax.c2p(2, 0))
        x1 = MathTex(r'x_{1}', color=azul).move_to(ax.c2p(2, 3)).scale(0.75)
        self.add(raiz1, x1)
        self.wait(1)

        
        # Se mueve la cámara para ver la gráfica completa
        self.play(
            self.camera.frame.animate.scale(2).move_to(np.array([0, 0, 0]))
            
        )
        raices1 = Text(r'Tenemos una raíz de multiplicidad tres', color=azul).move_to(ax.c2p(2, -10)).scale(0.75)
        raices2 = MathTex(r'x_{1} = x_{2} = x_{3} = 2', color=azul).move_to(ax.c2p(2, -15))
        self.add(raices1, raices2)
        self.wait(3)