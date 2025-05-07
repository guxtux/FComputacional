from manim import *

class CodeFromString(Scene):
    def construct(self):
        code = '''
import numpy as np

n = 3
x0 = np.array([1.5, 2.5, 3.5])
x = np.array([1., 2., 3., 4.])
f = np.array([0.671, 0.620, 0.567, 0.512])

for k in x0:
    yres = 0
    for i in range(0, n + 1):
        z = 1.0
        for j in range(0, n + 1):
            if i != j:
                z = z * (k - x[j])/(x[i] - x[j])
        yres = yres + z * f[i] 
    
    print ('El polinomio evaluado en P ({0:}) = {1:}'.format(k,  yres))'''

# https://pygments.org/styles/
        rendered_code = Code(
            code_string=code,
            tab_width=4,
            # font='Monospace',
            formatter_style='material',
            language='python',
            background='window',
            background_config={'stroke_color': 'maroon'},
            paragraph_config={"font": "Roboto Mono for Powerline",
                              "line_spacing": 1,},
            # line_spacing=1,
        ).scale(0.8)
        self.add(rendered_code)
        # self.play(Write(rendered_code), run_time=5)
        # self.wait(3)