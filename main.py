from newton import Newton
import math


def key(x):
    return math.log(x*x, math.e) - math.sin(x) - 2


def main():
    n = Newton(key, 10^-5)


if __name__ == "__main__":
    main()