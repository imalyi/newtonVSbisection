from method import Method


class Newton(Method):
    def __init__(self, key: callable, e: float) -> None:
        self.key = key
        self.e = e

    def solution(self) -> (float, int):
        x_prev = 0
        x = 1
        steps = 0
        while not self._check_diff(x, x_prev):
            tmp = self._calc_next_x(x_prev, x)
            x_prev = x
            x = tmp
            steps += 1
        return x, steps
    def generate_chart(self):
        return 0

    def step_number(self) -> int:
        return 0

    def _calc_next_x(self, x_prev: float, x: float) -> float:
        return x - ((self.key(x) * (x-x_prev)) / (self.key(x) - self.key(x_prev)))

    def _check_diff(self, x, x_prev):
        self.diff = abs(x-x_prev)
        return self.diff < self.e


import math
def key(x):
    return x*x - 2


if __name__ == "__main__":
    n = Newton(key, math.pow(10, -12))
    print(n.solution())