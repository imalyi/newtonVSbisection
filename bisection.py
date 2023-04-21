from method import Method


class Bisection(Method):
    def __init__(self, key: callable, section, e: float) -> None:
        self.section = section
        self.e = e
        self.function = key
        pass

    def solution(self) -> (float,int):
        # Function returns the root of the equation and the number of steps needed to reach the answer.
        if(self.function(self.section[0])*self.function(self.section[1])>=0):
            print("Błąd! f(a)*f(b)>=0. Proszę wybrać inny przedział [a,b].")
            return 0,0
        c = 1
        i = 0
        while self.function(c)!=0 and self.section[1]-self.section[0]>self.e:
            c = (self.section[0]+self.section[1])/2
            if self.function(self.section[0])*self.function(c)<0:
                self.section[1]=c
            elif self.function(self.section[1])*self.function(c)<0:
                self.section[0]=c
            i=i+1
        return c,i

    def generate_chart(self):
        return