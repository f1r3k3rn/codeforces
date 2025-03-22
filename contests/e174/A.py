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
        sol = True

        for i in range(1,n - 3):
            if vet[i] == 0 and vet[i - 1] == 1 and vet[i + 1] == 1:
                sol = False

        if sol:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()
