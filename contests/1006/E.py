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

        a,b = inlt()

        sol = []
        sol += [b]

        for i in range(1, a - 1):

            if a % 2 != 0:
                sol += [0]
            else:
                sol += [a]

        if a > 1:
            sol += [b]

        print(" ".join(map(str, sol)))





if __name__ == "__main__":
    main()
