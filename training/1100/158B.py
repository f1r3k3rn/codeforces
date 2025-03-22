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
    t = 1

    for _ in range(t):
        n = inp()
        vet = inlt()

        vet.sort()
        sol = 0

        k = [0] * 5

        for i in range(n):
            k[vet[i]] += 1

        while k[4] > 0:
            k[4] -= 1
            sol += 1

        while k[3] > 0 and k[1] > 0:
            k[3] -= 1
            k[1] -= 1
            sol += 1

        while k[2] > 0 and k[1] > 0:
            k[2] -= 1
            k[1] -= 2
            sol += 1

        while k[3] > 0:
            k[3] -= 1
            sol += 1

        while k[2] > 0:
            k[2] -= 2
            sol += 1

        while k[1] > 0:
            k[1] -= 4
            sol += 1

        print(sol)


if __name__ == "__main__":
    main()
