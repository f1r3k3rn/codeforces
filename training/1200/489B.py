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
        m = inp()
        ret = inlt()

        vet.sort()
        ret.sort()

        sol = 0
        j = 0
        for i in range(n):

            if j < m and vet[i] > ret[j]:
                while j < m and vet[i] - ret[j] > 1:
                    j += 1

            if j < m and abs(vet[i] - ret[j]) <= 1:
                sol += 1
                j += 1

        print(sol)


if __name__ == "__main__":
    main()
