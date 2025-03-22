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
        x = inp()
        sol = 10

        if "7" in str(x):
            sol = 0

        for i in range(1,10):

            k = int("9" * i)

            for i in range(1,10):
                f = x + k * i
                f = str(f)

                if "7" in f:
                    sol = min(sol,i)

        print(sol)



if __name__ == "__main__":
    main()
