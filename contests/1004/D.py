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
        vet = inlt()


        print("? 1 " + str(n))
        sys.stdout.flush()

        k1 = inp()


        print("? " + str(n) + " 1")
        sys.stdout.flush()

        k2 = inp()


        if k1 != k2 and k1 != 0:
            print("! A")
        else:
            print("! B")


if __name__ == "__main__":
    main()
