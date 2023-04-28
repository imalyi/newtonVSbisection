from method import Method


class AnswerNotFound(Exception):
    pass

class Answer:
    def __init__(self, method: Method, a: float, b: float, y: float, steps: int):
        self.method = method
        self.a = a
        self.b = b
        self.y = y
        self.steps = steps
class Answers:
    def __init__(self, e: float):
        """e potrzebne zeby odrozniac odpowiedzi. np -4.28125621847702 = -4.281256222626612 przy dokladnosci 10^-8"""
        self._answers = []
        self.e = e

    def add_answer(self, method: Method, a: float, b: float, y: float, steps: int) -> None:
        for answer in self._answers:
            answ = self._get_answer()
            if answ and answer:

        self._answers.append(Answer(method, a, b, y, steps))

    def _get_answer(self, y) -> Answer:
        for answer in self._answers:
            if abs(answer.y-y) < self.e:
                return answer
        raise AnswerNotFound