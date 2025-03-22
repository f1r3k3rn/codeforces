import sys
import heapq
from collections import defaultdict
from operator import index

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
    n = inp()
    vet = inlt()
    lh = vet[:n//2]
    rh = vet[n//2:]

    k = lh.index(max(lh))
    l = rh.index(max(rh))

    if lh[k] < rh[l]:
        print(l + n//2 , k )
    else:
        print(k , l + n//2)




if __name__ == "__main__":
    main()
