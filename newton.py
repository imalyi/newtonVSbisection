from method import Method


class Newton(Method):
    def __init__(self, key: callable, x_1: float, x_2: float, e: float) -> None:
        self.key = key
        self.e = e
        self.x_1 = x_1
        self.x_2 = x_2

    def solution(self) -> (float, int):
        steps = 0
        while not self._check_diff(self.x_2, self.x_1):
            tmp = self._calc_next_x(self.x_1, self.x_2)
            self.x_1 = self.x_2
            self.x_2 = tmp
            steps += 1
        return self.x_2, steps

    def _calc_next_x(self, x_prev: float, x: float) -> float:
        return x - ((self.key(x) * (x-x_prev)) / (self.key(x) - self.key(x_prev)))

    def _check_diff(self, x, x_prev):
        self.diff = abs(x-x_prev)
        return self.diff < self.e


if __name__ == "__main__":
    print("Test example: x^2 - 2 = 0")
    n = Newton(lambda x: x*x -2 , 1, 2, pow(10, -12))
    print(n.solution())
    #(1.414213562373095, 7)