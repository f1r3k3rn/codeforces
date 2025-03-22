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

    return list(map(int,s[:len(s) - 1]))


def invr():
    return map(int, input().split())


def main():
    t = inp()

    for _ in range(t):
        vet = [insr() for _ in range(9)]
        sus = 0
        for i in range(9):
            for j in range(9):
                if vet[i][j] == 1:
                    vet[i][j] = 2

        print("\n".join(["".join(map(str, x)) for x in vet]))

if __name__ == "__main__":
    main()
