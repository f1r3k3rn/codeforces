import sys
import heapq
from collections import defaultdict
import bisect

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
    t = 1

    for _ in range(t):
        n = inp()
        vet = inlt()
        q = inp()
        asked = inlt()

        pre = [0] * n

        pre[0] = vet[0]

        for i in range(1,n):
            pre[i] = pre[i-1] + vet[i]

        for i in range(q):
            idx = bisect.bisect_left(pre,asked[i])
            print(idx + 1)


if __name__ == "__main__":
    main()
