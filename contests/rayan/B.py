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


# WRITE HERE
def solve(n,m,k,fortress):
    sol = 0
    limit = 0
    bonus = 0
    for i in range(len(fortress)):
        if bonus > 0:
            bonus -= 1
            continue

        if fortress[i] == "1":
            limit = 0
        else:
            limit += 1

        if limit == m:
            sol += 1
            limit = 0
            bonus = k - 1

    return sol


# WRITE HERE

def main():
    t = inp()

    for _ in range(t):
        n,m,k = inlt()
        fortress = insr()
        print(solve(n,m,k,fortress))


if __name__ == "__main__":
    main()
