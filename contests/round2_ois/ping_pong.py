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
    a,b,c = inp(), inp(), inp()

    print(b * 3 + c * 2 + a)
    print(b + c + a)


if __name__ == "__main__":
    main()
