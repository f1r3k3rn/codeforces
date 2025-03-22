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
        n,a,b,c = inlt()

        sol  = n // (a + b + c) * 3
        r = n % (a + b + c)

        if r > 0 and r <= a:
            sol += 1
        elif r > a and r <= a + b:
            sol += 2
        elif r > a + b and r <= a + b + c:
            sol += 3

        print(sol)

if __name__ == "__main__":
    main()
