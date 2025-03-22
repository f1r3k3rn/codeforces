import sys
import heapq
from collections import defaultdict
from math import ceil

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
def intersection(l1,r1,l2,r2):
    if l1 > r2 or l2 > r1:
        return []
    return [max(l1,l2),min(r1,r2)]


# WRITE HERE

def main():
    t = inp()

    for _ in range(t):
        k,l,r,l2,r2 = inlt()
        sol = 0

        e = 0
        while r2 // k ** e >= l:
            ran2 = intersection(l,r, ceil(l2 // k ** e), r2 // k ** e)
            if len(ran2) != 0:
                sol += ran2[1] - ran2[0] + 1
            e += 1

        print(sol)

if __name__ == "__main__":
    main()