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
def solve(n, k , vet):
    m = vet[n - 1]
    sol = 1
    s = defaultdict(int)

    for i in vet:
        s[i] += 1

    g = [s[i] for i in s.keys()]
    g.sort()
    sol = len(s)
    for i in g:
        if i <= k:
            k -= i
            sol -= 1
            sol = max(sol, 1)

    return sol


# WRITE HERE

def main():
    t = inp()

    for _ in range(t):
        n, k = inlt()
        vet = inlt()
        print(solve(n, k , vet))


if __name__ == "__main__":
    main()
