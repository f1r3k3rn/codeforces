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


def main():
    t = inp()

    for _ in range(t):

        n = inp()
        vet = inlt()

        pfx = [0] * n
        pfx[0] = vet[0]

        for i in range(1, n):
            pfx[i] = pfx[i - 1] + vet[i]

        sol = 0
        for i in range(n):
            if abs(pfx[i]) + pfx[n - 1] - pfx[i] > sol:
                sol = abs(pfx[i]) + pfx[n - 1] - pfx[i]

        print(sol)

if __name__ == "__main__":
    main()
