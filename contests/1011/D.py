import sys
import heapq
from collections import defaultdict
import math

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
        x,y = inlt()

        k = 57 * 56 // 2

        binx, biny = bin(x)[2:], bin(y)[2:]

        print(binx, biny)

        for i in range(0, len(binx)):
            for j in range(0, len(biny)):









if __name__ == "__main__":
    main()
