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

        k = 0

        dp = [[0] * 10 for _ in range(4)]

        dp[0][0] = 1

        for i in range(n):
            for j in range(3, 0, -1):
                for k in range(10):
                    dp[j][k] = max(dp[j - 1][(k - vet[i] % 10 + 10) % 10],dp[j][k])


        if dp[3][3] == 1:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()
