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
    e = 0
    while e==0:
        print("Wpisz e")
        e = float(input())
        if e<=0 or e>=1:
            print("Dokładność nie mieści się w przedziale (0;1)")
            e = 0
    print("Wpisz a (początek przedziału)")
    a = float(input())
    print("Wpisz b (koniec przedziału)")
    b = float(input())
    bisect = Bisection(key, [a, b], e)
    answer = bisect.solution()
    if answer[1]>0:
        print("Bisekcja: Pierwiastek równania to ", answer[0], ",obliczone w ", answer[1], " krokach.")
    try:
        newton = Newton(key,a,b,e)
        answer2 = newton.solution()
        print("Newton: Pierwiastek równania to ", answer2[0], ",obliczone w ", answer2[1], " krokach.")
        if answer2[0]-answer[0]>e:
            print("Uwaga, prawdopodobnie na przedziale [",a,",",b,"] znajduje sie więcej niż jeden punkt zerowy funkcji.")
    except IterationLimit:
        pass



def findAllRoots(a,b,precision):
    c = b
    answers = []
    while c>=a:
        c -= precision
        if key(b)*key(c)<0:
            bisect = Bisection(key,[c,b],math.pow(10,-8))
            answer = bisect.solution()
            answers.append(answer)
            try:
                newton = Newton(key, b, c, math.pow(10,-8))
                answer = newton.solution()
                answers.append(answer)
            except IterationLimit:
                pass
            b = c
    answers = sorted(answers, key=lambda x: x[0], reverse=False)
    for x in answers:
        print(x[2],": Pierwiastek = ",x[0],"Obliczone w",x[1],"krokach.")

def main():
    cont = True
    while cont:
        menu()
        try:
            choice = int(input())
            if choice == 1:
                findRoot()
            elif choice == 2:
                findAllRoots(-10, 10, 0.001)
            elif choice == 3:
                cont = False
            else:
                print("Nieprawidłowa wartość. Podaj liczbę 1, 2 lub 3.")
        except ValueError:
            print("Nieprawidłowy znak. Podaj liczbę 1, 2 lub 3.")



if __name__ == "__main__":
    main()
