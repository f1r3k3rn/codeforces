import sys
import heapq
from collections import defaultdict
import math

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

def intersect(l,r,a,b):
    return max(0,min(r,b) - max(l,a) + 1)


def main():
    t = inp()

    for _ in range(t):
        l,r = inlt()

        sol = 0
        flag = False

        num = l
        while num > 0:
            num //= 3
            sol += 2


        e, i = 1, 1

        while i <=  r:
            i *= 3

            sol += intersect(l + 1,r,i//3,i - 1) * e

            e += 1


        print(sol)


if __name__ == "__main__":
    main()
