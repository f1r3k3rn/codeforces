import sys
import heapq
from collections import defaultdict
import math
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



def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

# WRITE HERE
def solve(a,b):
    return lcm(a,b)


# WRITE HERE

def main():
    t = inp()

    for _ in range(t):
        a,b = inlt()
        print(solve(a,b))


if __name__ == "__main__":
    main()
