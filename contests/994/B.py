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
    sol = "YES"
    s = False
    p = False

    if vet[0] == "s" :
        vet = vet[1:]
        n -= 1

    if n > 0 and vet[-1] == "p":
        vet = vet[:-1]
        n -= 1

    for i in range(n):
        if vet[i] == "s":
            if p:
                sol = "NO"
                break
            else:
                s = True
        elif vet[i] == "p":
            if s:
                sol = "NO"
                break
            else:
                p = True

    return sol


# WRITE HERE

def main():
    t = inp()

    for _ in range(t):
        n = inp()
        vet = insr()
        print(solve(n, vet))


if __name__ == "__main__":
    main()
