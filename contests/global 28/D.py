import sys
import heapq
from collections import defaultdict
from bisect import bisect_left, bisect_right
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
def solve(n,m,a,b):
    sol = []

    b.sort()
    cap = a[0]
    a.sort()

    for i in range(n):
        if a[i] > cap:
            a = a[i:]
            break

    search = bisect_left(b,cap + 1) - 1


    for i in range(1,m + 1):
        temp = a[search:] + a[:search + m % i]

        sol = 0
        for j in range(0,temp,i):
            if
                sol += pf[j]

        print(sol)












    return " ".join(map(str,sol))


# WRITE HERE

def main():
    t = inp()

    for _ in range(t):
        n,m = inlt()
        a = inlt()
        b = inlt()

        print(solve(n,m,a,b))


if __name__ == "__main__":
    main()
