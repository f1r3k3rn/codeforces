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
    t = inp()

    for _ in range(t):
        n = inp()
        vet = inlt()

        dp = [[0] * n for _ in range(3)]

        mod = 998244353

        for i in range(n):

            if i > 0:
                dp[0][i] += dp[0][i - 1]
                dp[1][i] += dp[1][i - 1]
                dp[2][i] += dp[2][i - 1]

            if vet[i] == 1:
                dp[0][i] += 1
                dp[0][i] %= mod

            if vet[i] == 2 and i > 0:
                dp[1][i] = (dp[1][i] * 2 + dp[0][i - 1]) % mod

            if vet[i] == 3 and i > 0:
                dp[2][i] = (dp[2][i]  + dp[1][i - 1]) % mod

        print(dp[2][n - 1])








if __name__ == "__main__":
    main()
