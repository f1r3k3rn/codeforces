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

        pressed = [(0,0)] * n

        for i in range(n):
            x,y = inlt()

            pressed[i] = (x,y)

        x,y = 0,0

        for i in range(n):

            x += pressed[i][0]
            y += pressed[i][1]

        print((x + m - pressed[0][0])* 2 + (y + m - pressed[0][1]) * 2)







if __name__ == "__main__":
    main()
