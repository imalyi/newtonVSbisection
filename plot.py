from newton import Newton
from bisection import Bisection


class PlotData:
    def __init__(self, newton: Newton, bisection: Bisection):
        self.newton = newton
        self.bisection = bisection
        self.newton_steps = []
        self.bisection_steps = []

    for i in range(14):
