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
def solve(n, bs):

    start = 0
    sol = 0
    flip = "1"

    for i in range(start,len(bs)):
        if bs[i] == flip:
            sol += 1
            flip = "1" if flip == "0" else "0"


    return sol


# WRITE HERE

def main():
    t = inp()

    for _ in range(t):
        n = inp()
        bs = insr()
        print(solve(n, bs))


if __name__ == "__main__":
    main()
