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
def solve(a,b,c):

    dp = [[10**7 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
    dp[0][0] = 0

    for i in range(len(a) + 1):
        for j in range(len(b) + 1):
            if i > 0:
                dp[i][j] = min(dp[i][j], dp[i-1][j] + int(a[i - 1] != c[i + j - 1]))
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j-1] + int(b[j - 1] != c[i + j - 1]))

    return dp[len(a)][len(b)]


# WRITE HERE

def main():
    t = inp()

    for _ in range(t):
        a,b,c, = insr(), insr(), insr()
        print(solve(a,b,c))


if __name__ == "__main__":
    main()
