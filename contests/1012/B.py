import sys
import heapq
from collections import defaultdict
from sys import flags

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

        mat = [[] for i in range(n)]
        mask = [['0' for j in range(m)] for i in range(n)]

        for i in range(n):
            mat[i] = insr()


        for i in range(n):
            for j in range(m):
                if mat[i][j] == '0':
                    break
                mask[i][j] = '1'


        for j in range(m):
            for i in range(n):
                if mat[i][j] == '0':
                    break
                mask[i][j] = '1'

        flag = 1
        for i in range(n):
            for j in range(m):
                flag &= mask[i][j] == mat[i][j]


        print('YES' if flag == 1 else 'NO')


if __name__ == "__main__":
    main()
