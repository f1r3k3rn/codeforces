import sys
import heapq
from collections import defaultdict
import itertools

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
def solve(n):
    vet = [(i + 1) for i in range(n)]
    max_val = 0
    for i in range(n):
        max_val += vet[i]
        for j in range(i + 1, n):
            x = 10000
            for k in range(i, j + 1):
                x = min(x, vet[k])
            max_val += x

    for perm in itertools.permutations(vet):
        val = 0
        for i in range(n):
            val += perm[i]
            for j in range(i + 1, n):
                x = 10000
                for k in range(i, j + 1):
                    x = min(x, perm[k])
                val += x

        if val == max_val:
            print(perm)




# WRITE HERE

def main():
    t = inp()

    for _ in range(t):
        n = inp()
        print(solve(n))


if __name__ == "__main__":
    main()
