from manim import *

class ResultadoTerminal(Scene):
    def construct(self):
        # Simulación de la terminal
        terminal_output = '''
El polinomio evaluado en P( 1.5 ) = 0.64575
El polinomio evaluado en P( 2.5 ) = 0.59375
El polinomio evaluado en P( 3.5 ) = 0.53975
'''

        # Texto con estilo terminal
        terminal = Code(
            code_string=terminal_output,
            language="bash",  # puede ser "text" o "bash"
            background="rectangle",
            # font="Monospace",
            formatter_style="monokai",
            paragraph_config={"font": "Monospace",
                "line_spacing": 1,},
        ).scale(0.75)

        marco = SurroundingRectangle(terminal, color=WHITE, buff=0.3)

        # Título
        titulo = Text("Salida de terminal - Interpolación puntos", font_size=36).to_edge(UP)

        # Añadir todo
        self.add(titulo, marco, terminal)
