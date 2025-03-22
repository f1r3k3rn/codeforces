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

        print(k // (n - 1) * n + k % (n - 1) - 1 if k % (n - 1) == 0 else k // (n - 1) * n + k % (n - 1))


if __name__ == "__main__":
    main()
