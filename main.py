from newton import Newton
from bisection import Bisection
import math
from newton import IterationLimit

def key(x):
    return math.log(x*x, math.e) - math.sin(x) - 2

def menu():
    print("Menu:\n")
    print("1. Znajdź pierwiastek")
    print("2. Znajdź wszystkie pierwiastki")
    print("3. Wyjdź")

def findRoot():
    print("Wpisz e")
    e = float(input())
    print("Wpisz a (początek przedziału)")
    a = float(input())
    print("Wpisz b (koniec przedziału)")
    b = float(input())
    bisect = Bisection(key, [a, b], e)
    answer = bisect.solution()
    print("Bisekcja: Pierwiastek równania to ", answer[0], ",obliczone w ", answer[1], " krokach.")
    try:
        newton = Newton(key,a,b,e)
        answer = newton.solution()
        print("Newton: Pierwiastek równania to ", answer[0], ",obliczone w ", answer[1], " krokach.")
    except IterationLimit:
        pass



def findAllRoots(a,b,precision):
    c = a
    while c<=b:
        c += precision
        if key(a)*key(c)<0:
            bisect = Bisection(key,[a,c],math.pow(10,-8))
            answer = bisect.solution()
            print("Bisekcja: Pierwiastek równania to ", answer[0], ",obliczone w ", answer[1], " krokach.")
            try:
                newton = Newton(key, a, b, math.pow(10,-8))
                answer = newton.solution()
                print("Newton: Pierwiastek równania to ", answer[0], ",obliczone w ", answer[1], " krokach.")
            except IterationLimit:
                pass
            a = c

def main():
    cont = True
    while(cont):
        menu()
        choice = int(input())
        if choice == 1:
            findRoot()
        if choice == 2:
            findAllRoots(-10,10,0.001)
        if choice == 3:
            cont = False


if __name__ == "__main__":
    main()
