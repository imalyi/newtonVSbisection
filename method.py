from abc import ABC, abstractmethod


class Method(ABC):
    @abstractmethod
    def solution(self):
        pass
