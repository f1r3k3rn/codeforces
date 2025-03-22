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
        n,k = inlt()

        sol = 0

        if n % 2 == 1:
            sol += 1
            n -= k

        sol += n // (k - 1)

        if n % (k - 1) != 0:
            sol += 1

        print(sol)




if __name__ == "__main__":
    main()
