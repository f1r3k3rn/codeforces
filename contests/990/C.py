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


# WRITE HERE
def solve(n,mat):

    sol = - (10**10)
    piv = 0

    for j in range(0,n):
        piv += max(mat[0][j], mat[1][j])

    for i in range(0, n):
        if sol < (piv + min(mat[0][i], mat[1][i])):
            sol = piv + min(mat[0][i], mat[1][i])

    return sol


# WRITE HERE

def main():
    t = inp()

    for _ in range(t):
        n = inp()
        mat = [inlt() for i in range(2)]
        print(solve(n, mat))


if __name__ == "__main__":
    main()
