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
def solve(n, vet):

    dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):

        k = 0
        for j in range(i + 1, n):
            if vet[j] < vet[i]:
                k += 1
            dp[i][i] = k

        for j in range(i + 1, n):

            if vet[j] < vet[i]:
                k -= 1
            elif vet[j] > vet[i]:
                k += 1

            dp[i][j] = k


    sol = 0
    rsol = 0

    kk,jj = 0,0

    for i in range(n):
        sol += dp[i][i]

    rsol = sol

    for i in range(n):
        for j in range(i, n):

            if rsol > sol - dp[i][i] + dp[i][j]:
                rsol = sol - dp[i][i]  + dp[i][j]
                kk,jj = i,j


    return "{} {}".format(kk + 1, jj + 1)


# WRITE HERE

def main():
    t = inp()

    for _ in range(t):
        n = inp()
        vet = inlt()
        print(solve(n, vet))




if __name__ == "__main__":
    main()
