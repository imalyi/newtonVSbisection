from method import Method


class Bisection(Method):
    def __init__(self, key: callable, section, e: float) -> None:
        self.section = section
        self.e = e
        self.function = key
        pass

    def solution(self) -> (float, int):
        if self.section[0]==0 or self.section[1]==0:
            print("Błąd! Funkcja jest nieokreślona w punkcie 0. Proszę wybrać punkty a,b różne od 0.")
            return 0, 0
        if (self.function(self.section[0]) * self.function(self.section[1]) >= 0):
            print("Bisekcja: Błąd! f(a)*f(b)>=0. Proszę wybrać inny przedział [a,b].")
            return 0, 0
        c = 1
        step = 0
        while self.function(c) != 0 and self.section[1] - self.section[0] > self.e:
            c = (self.section[0] + self.section[1]) / 2
            if self.function(self.section[0]) * self.function(c) < 0:
                self.section[1] = c
            else:
                self.section[0] = c
            step = step + 1
        return c, step, "Bisekcja"

