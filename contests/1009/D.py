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


def calculate(x,rad):
    l,r = 0,rad

    while l <= r:
        m = (l + r) // 2
        if m * m <= rad * rad - x * x:
            s = m
            l = m + 1
        else:
            r = m - 1

    return l * 2 - 1

def main():
    t = inp()

    for _ in range(t):
        n,m = inlt()
        xs = inlt()
        rs = inlt()

        points = [(x,y) for x,y in zip(xs,rs)]
        points.sort(key=lambda x: x[0])

        q = defaultdict(int)

        for p in points:
            x,r = p

            for i in range(r):
                f = calculate(r - i,r)
                q[x - r + i] = max(f, q[x - r + i])
                q[x + r - i] = max(f, q[x + r - i])

            q[x] = max(calculate(0,r), q[x])

        print(sum(q.values()))

if __name__ == "__main__":
    main()
