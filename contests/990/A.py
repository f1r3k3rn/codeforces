import sys
import heapq
from collections import defaultdict
from math import isqrt

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
    s = 0
    for i in vet:
        s += i
        if isqrt(s) ** 2 == s and s % 2 == 1:
            sol += 1


    return sol


# WRITE HERE

def main():
    t = inp()

    for _ in range(t):
        n = inp()
        vet = inlt()
        print(solve(n, vet))


if __name__ == "__main__":
    main()
