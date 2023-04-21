from newton import Newton
from bisection import Bisection
import math


def key(x):
    return math.log(x*x, math.e) - math.sin(x) - 2


def main():
    b = Bisection(key,[-2.5,-1],math.pow(10,-5))
    answer=b.solution()
    print("Bisection: Answer is ",answer[0]," in ",answer[1]," steps")
    #n = Newton(key, 10^-5)


if __name__ == "__main__":
    main()