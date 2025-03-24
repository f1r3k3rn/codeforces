import sys
import heapq
from collections import defaultdict
from bisect import bisect_left, bisect_right

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

        if x == y :
            print(-1)
        else:
            print((1 << 51) - max(x,y))




if __name__ == "__main__":
    main()
