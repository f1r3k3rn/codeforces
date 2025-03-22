import sys
import heapq
from collections import defaultdict
from math import floor

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
        n,k,p = inlt()

        if k >= -n * p and k <= n * p:
            print(abs(k) // p + (1 if k % p != 0 else 0))
        else:
            print(-1)

if __name__ == "__main__":
    main()
