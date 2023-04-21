from abc import ABC, abstractmethod


class Method(ABC):
    """Interface for class with newton and bisection method realization"""
    @abstractmethod
    def solution(self):
        pass
