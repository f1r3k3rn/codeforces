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
        x,y,a = inlt()

        a -= (a // (x + y)) * (x + y)

        if (a + 1) <= x:
            print('NO')
        else:
            print('YES')




if __name__ == "__main__":
    main()
