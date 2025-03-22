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
def solve(x, m):

    sol = 0


    sol = m // x

    if (m // x) * x > m :
        sol -= 1

    for i in range(1,min(x * 2) + 1):
        if (x ^ i) % i == 0 and (x ^ i) % x != 0:
            sol += 1

    return sol


# WRITE HERE

def main():
    t = inp()

    for _ in range(t):

        x,m = inlt()
        print(solve(x,m))


if __name__ == "__main__":
    main()
