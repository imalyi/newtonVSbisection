from abc import ABC, abstractmethod


class Method(ABC):
    """Interface for class with newton and bisection method realization"""
    @abstractmethod
    def solution(self):
        pass

    @abstractmethod
    def generate_chart(self):
        """Generate chart and return chart object"""

    @abstractmethod
    def step_number(self) -> int:
        """Return step number"""
        pass

