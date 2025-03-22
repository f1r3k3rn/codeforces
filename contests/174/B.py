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
        n,d = inlt()

        divisibility = [1]


        if d == 3 or d == 9 or d == 6 or n >= 3:
            divisibility.append(3)

        if d == 5:
            divisibility.append(5)

        if d == 7:
            divisibility.append(7)

        if (d == 3 or d == 9 or d == 6 and n >= 3) or n >= 4:
            divisibility.append(9)


        print(" ".join(map(str,divisibility)))


if __name__ == "__main__":
    main()
