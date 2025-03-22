import sys
import heapq
from collections import defaultdict
from math import log2
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

        k = 1
        sol = 1
        while k < n:
            sol += 1
            k = 2 * k + 2

        print(sol)



if __name__ == "__main__":
    main()
