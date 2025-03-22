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
        ret = inlt()

        s = [vet[i] - ret[i + 1]  for i in range(n - 1)]

        k = 0
        for i in s:
            if i > 0:
                k += i

        print(vet[n - 1] + k)


if __name__ == "__main__":
    main()
