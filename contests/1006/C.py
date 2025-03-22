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

def main():
    t = inp()

    for _ in range(t):
        a,b = inlt()

        sol = [0] * a
        for i in range(a):

            if b | i == b:
                sol[i] = i
            else:
                sol[i] = b

        orr = 0
        for i in range(a):
            orr |= sol[i]

        if orr != b:
            sol[a - 1] = b

        print(" ".join(map(str, sol)))




if __name__ == "__main__":
    main()
