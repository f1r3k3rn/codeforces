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
    s = set()

    for i in range(1, n + 1):
        s.add(i)

    c = [0 for i in range(n)]

    for i in range(n):
        if vet[i] in s:
            c[i] = vet[i]
            s.remove(vet[i])

    q = []
    for k in s:
        q.append(k)

    for i in range(n):
        if c[i] == 0:
            c[i] = q.pop()

    return " ".join(map(str,c))


# WRITE HERE

def main():
    t = inp()

    for _ in range(t):
        n = inp()
        vet = inlt()
        print(solve(n, vet))


if __name__ == "__main__":
    main()
