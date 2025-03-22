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
def solve(n,k):
    sol = 0

    vet = [0] * n

    start = 1

    for i in range(1,n + 1):

        if i * k - 1 >= n:
            break
        vet[i * k - 1] = i
        start += 1

    for i in range(n):
        if vet[i] == 0:
            vet[i] = start
            start += 1

    return " ".join(map(str, vet))


# WRITE HERE

def main():
    t = inp()

    for _ in range(t):
        a,b = inlt()
        print(solve(a,b))


if __name__ == "__main__":
    main()
