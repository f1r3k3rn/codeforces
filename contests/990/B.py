import sys
import heapq
from collections import defaultdict
from math import factorial
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

    lower_case = "abcdefghijklmnopqrstuvwxyz"
    reworked = ""

    for i in lower_case:
        if i in vet:
            reworked += i

    best = ""
    bestv = 0


    for i in range(n):
        for j in reworked:
            ret = vet[:i] + [j] + vet[i+1:]

            dn = 1
            for j in lower_case:
                dn *= factorial(ret.count(j))

            if dn > bestv:
                best = ret
                bestv = dn

    return  "".join(best)


# WRITE HERE

def main():
    t = inp()

    for _ in range(t):
        n = inp()
        vet = insr()
        print(solve(n, vet))


if __name__ == "__main__":
    main()
