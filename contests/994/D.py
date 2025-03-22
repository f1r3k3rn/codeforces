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
def solve(n,m,k,mat):

    dp = [[[10**12 for _ in range(m)] for _ in range(m)] for _ in range(n)]

    print(dp)
    for l in range(m):
        dp[0][0][l] = min(dp[0][0][l],mat[0][l] + k * l)

    for i in range(n - 1):
        for j in range(m - 1):
            for l in range(m):
                dp[i][j + 1][l] = min(dp[i][j + 1][l],dp[i][j][l] + mat[i][(j + l + 1) % m])

            inz = [10**12 for _ in range(m)]
            for l in range(m):
                inz[l] = min(inz[l],mat[i][(j + l) % m] + l*k)

            for l in range(m):
                dp[i + 1][j][l] = min(dp[i + 1][j][l],dp[i][j][l] + inz[j])


    return min(dp[n - 1][m - 1])

# WRITE HERE

def main():
    t = inp()

    for _ in range(t):
        n,m,k = inlt()
        mat = [inlt() for _ in range(n)]
        print(solve(n,m,k,mat))


if __name__ == "__main__":
    main()
