import numpy as np
from manim import *
from scipy import interpolate
from scipy.interpolate import interp1d


def generate_random_curves(n):
    x = np.array([0, 0.2, 0.4, 0.8, 0.7, 0.2, 0.0])
    y = np.array([0, 0.1, 0.2, 0.9, 1, 0.25, 0])
    curves = []
    for i in range(n):
        rnd_x = np.random.uniform(-0.1, 0.1, 7)
        rnd_y = np.random.uniform(-0.1, 0.1, 7)
        rnd_x[0] = 0
        rnd_y[0] = 0
        rnd_x[-1] = 0
        rnd_y[-1] = 0

        perterb_x = x + rnd_x
        perterb_y = y + rnd_y

        curves.append([perterb_x, perterb_y])

    return curves


class Intro(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 1, 10], y_range=[0, 1, 10], axis_config={"include_tip": False}
        )
        labels = ax.get_axis_labels(x_label="d", y_label="a")

        t = ValueTracker(0)

        tx, ty = generate_random_curves(1)[0]
        tck, u = interpolate.splprep([tx, ty], s=0)

        eval_pts = np.linspace(0, 1, 1000)

        smooth_tx,smooth_ty = interpolate.splev(eval_pts, tck)

        initial_point = [ax.coords_to_point(t.get_value(), interpolate.splev(t.get_value(), tck)[1])]
        dot = Dot(point=initial_point)

        path = VMobject()
        path.set_points_as_corners([dot.get_center(), dot.get_center()])

        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)

        path.add_updater(update_path)
        dot.add_updater(lambda x: x.move_to(ax.c2p(smooth_tx[int(t.get_value())],
                                                   smooth_ty[int(t.get_value())])))



        self.add(ax, labels, dot, path)
        self.wait()
        self.play(t.animate.set_value(999), run_time=5)
        self.wait(10)

