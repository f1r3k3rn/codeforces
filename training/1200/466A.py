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
        n,m,a,b = inlt()

        sol = 10**9

        for i in range(1001):
            for j in range(1001):
                if i * a + j * b < sol and i + j * m >= n:
                    sol = i * a + j * b

        print(sol)


if __name__ == "__main__":
    main()
