import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline


def inp():
    return int(input())


def inlt():
    return list(map(int, input().split()))


def insr():
    s = input()
    return list(s[:len(s) - 1])


def invr():
    return map(int, input().split())

def isnotdegeneratetriangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def main():
    t = inp()

    for _ in range(t):
        x = inp()

        unos = zeros = 0

        f = x

        pot1, pot2 = 0, 0

        e = 1
        while f > 0:
            if f % 2 == 1:
                if pot1 == 0:
                    pot1 = e
                unos += 1
            else:
                if pot2 == 0:
                    pot2 = e
                zeros += 1
            f //= 2
            e *= 2

        if unos != 0 and zeros != 0 and unos > 1:
            print(pot2 + pot1)
        else:
            print(-1)





if __name__ == "__main__":
    main()
