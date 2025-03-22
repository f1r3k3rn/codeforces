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
def solve(n, vet):
    sol = 0
    return sol


# WRITE HERE

def main():
    t = inp()

    for _ in range(t):
        n = inp()
        s = insr()

        k = 0
        r = 0
        sol = 0


        for i in range(n):
            if s[i] == '-':
                k += 1
            else:
                r += 1

        sol += (k // 2) * r * (k // 2 + (1 if k % 2 == 1 else 0))

        print(sol)


if __name__ == "__main__":
    main()
