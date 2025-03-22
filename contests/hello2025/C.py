import sys
import heapq
from collections import defaultdict
from math import log2
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
def solve(n, vet):
    sol = 0
    return sol
    ## r


# WRITE HERE

def main():
    t = inp()

    for _ in range(t):
        l,r = inlt()

        a = r
        b = r - 1

        aa,bb = a,b

        c = 0
        r = 0
        while aa > 0 and bb > 0:
            if (bb % 2) == 0 or (bb % 2) == 0:
                c += 2**r
            r += 1
            aa //= 2
            bb //= 2

        if c < l:
            for i in range(log2(c) - 1):
                if (c & (1 << i)) == 0:
                    c += 1 << i
                    if c >= l:
                        break
            c = l

        print((a^b) + (b^c) + (a^c))

        f1,f2,f3 = inlt()

        print((f1^f2) + (f2^f3) + (f1^f3))


if __name__ == "__main__":
    main()
