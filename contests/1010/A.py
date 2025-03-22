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
        n,m = inlt()

        mat = [insr() for _ in range(n) ]

        column_xor = [0] * m
        row_xor = [0] * n

        for i in range(n):
            for j in range(m):
                row_xor[i]  ^= int(mat[i][j])
                column_xor[j] ^= int(mat[i][j])

        row_count = sum(row_xor)
        column_count = sum(column_xor)

        print(max(row_count, column_count))




if __name__ == "__main__":
    main()
