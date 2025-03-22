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
        sol = "NO"
        n = inp()
        vet = inlt()
        h1 = vet[::2]
        h2 = vet[1::2]
        s1 = sum(h1)
        s2 = sum(h2)
        s = sum(vet)

        if s % n == 0 and s1 // len(h1) == s2 // len(h2):
            sol = "YES"

        print(sol)




if __name__ == "__main__":
    main()
