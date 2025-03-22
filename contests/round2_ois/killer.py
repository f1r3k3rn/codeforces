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
def solve(n, k):
    s = 0
    sol = "NO"

    if n == k * (k + 1) // 2 or n == k * (k + 1) // 2 + 1 or k == 1:
        sol = "YES"

    return sol


# WRITE HERE

def main():
    t = inp()

    for _ in range(t):
        n,k = inlt()
        print(solve(n, k))


if __name__ == "__main__":
    main()
