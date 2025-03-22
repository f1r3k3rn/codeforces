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


def main():
    t = 1

    for _ in range(t):
        n = inp()
        vet = inlt()

        pfx = [0] * n
        pfx[0] = vet[0]
        for i in range(1,n):
            pfx[i] = pfx[i-1] + vet[i]

        ret = vet
        ret.sort()

        pfx_ret = [0] * n
        pfx_ret[0] = ret[0]
        for i in range(1,n):
            pfx_ret[i] = pfx_ret[i-1] + ret[i]

        q = inp()


        for i in range(q):
            type,l,r = inlt()

            if type == 1:
                print(pfx[r-1] - (pfx[l-2] if l > 1 else 0))
            else:
                print(pfx_ret[r-1] - (pfx_ret[l-2] if l > 1 else 0))

if __name__ == "__main__":
    main()
