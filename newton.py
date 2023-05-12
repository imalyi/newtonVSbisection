from method import Method


class IterationLimit(Exception):
    pass

class BadInterval(Exception):
    pass


class Newton(Method):
    def __init__(self, key: callable, x_1: float, x_2: float, e: float, max_step: int = 45) -> None:
        self.key = key
        self.e = e
        self.x_1 = x_1
        self.x_2 = x_2
        self.max_steps = max_step

    def solution(self) -> (float, int):
        steps = 0
        while not self._check_diff(self.x_2, self.x_1):
            if steps > self.max_steps:
                print("Metoda siecznych Newtona na podanym odcinku nie jest zbieżna.")
                raise IterationLimit
            try:
                tmp = self._calc_next_x(self.x_1, self.x_2)
            except ZeroDivisionError:
                raise BadInterval
            self.x_1 = self.x_2
            self.x_2 = tmp
            steps += 1
        return self.x_2, steps, "Newton"

    def _calc_next_x(self, x_prev: float, x: float) -> float:
        if x==0 or x_prev ==0:
            raise IterationLimit
        return x - ((self.key(x) * (x-x_prev)) / (self.key(x) - self.key(x_prev)))

    def _check_diff(self, x, x_prev):
        self.diff = abs(x-x_prev)
        return self.diff < self.e

    def __str__(self):
        return 'Newton'

