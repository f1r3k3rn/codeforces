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
def solve(n,m,strz):
    sol = 0
    s = 0
    for i in strz:
        if s + len(i) > m :
            break
        sol += 1
        s += len(i)


    return sol


# WRITE HERE

def main():
    t = inp()

    for _ in range(t):
        n,m = inlt()
        strz = []
        for _ in range(n):
            strz.append(insr())

        print(solve(n,m,strz))


if __name__ == "__main__":
    main()
