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
        n,x,y = inlt()
        vet = [0 if i % 2 == 0 else 1 for i in range(n)]

        if n % 2 == 0 :
            if vet[x - 1] == vet[y - 1]:
                vet[x - 1] = 2
        else:
            vet[-1] = 2
            if vet[x - 1] == vet[y - 1]:
                if vet[(x - 2)% n] == 2:
                    vet[(x - 2)% n] = vet[y - 1]
                if vet[x % n] == 2:
                    vet[x % n] = vet[y - 1]
                vet[x - 1] = 2

        print(" ".join(map(str,vet)))


if __name__ == "__main__":
    main()
