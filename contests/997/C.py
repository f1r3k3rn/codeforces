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
        sol = [0] * n

        sol[0] = sol[1] = 1

        for i in range(2, n - 1):
            sol[i] = i

        sol[n - 1] = 1

        print(" ".join(map(str, sol)))

        print(" ".join(map(str, sol)))


if __name__ == "__main__":
    main()
