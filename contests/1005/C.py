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


# WRITE HERE
def solve(n, vet):
    sol = 0
    return sol


# WRITE HERE

def main():
    t = inp()

    for _ in range(t):
        n = inp()
        vet = inlt()

        sol = 0
        x = 0
        px = 0
        y = 0
        psol = 0

        for i in range(0, len(vet)):
            r = vet[i] if vet[i] > 0 else -vet[i]
            if vet[i] > 0:
                x = 0
                y += r

            if vet[i] < 0:
                psol += r
                x += r

            psol = max(psol, x + y)

        x = 0
        px = 0
        y = 0
        qsol = 0

        for i in range(len(vet) - 1 , 0 , -1):
            r = vet[i] if vet[i] > 0 else -vet[i]
            if vet[i] < 0:
                x = 0
                y += r

            if vet[i] > 0:
                qsol += r
                x += r

            qsol = max(qsol, x + y)

        print(max(psol, qsol) + sol)


if __name__ == "__main__":
    main()
