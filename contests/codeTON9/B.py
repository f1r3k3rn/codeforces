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
def solve(a):
    sol = -1
    a = a.strip()
    for i in range(len(a) - 1):
        if a[i] == a[i + 1]:
            sol = a[i : i + 2]
        elif i < len(a) - 2 and a[i] != a[i + 1] and a[i + 1] != a[i + 2] and a[i] != a[i + 2]:
            sol = a[i : i + 3]

    return sol


# WRITE HERE

def main():
    t = inp()

    for _ in range(t):
        a = input()
        print(solve(a))


if __name__ == "__main__":
    main()
