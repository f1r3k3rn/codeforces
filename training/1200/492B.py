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

def main():
    t = 1

    for _ in range(t):
        n,l = inlt()
        vet = inlt()

        vet.sort()

        max_diff = 0
        for i in range(n):


            if i == 0:
                max_diff = vet[i]

            if i > 0:
                max_diff = max(max_diff,(vet[i] - vet[i-1]) / 2)

            if i < n-1:
                max_diff = max(max_diff,(vet[i+1] - vet[i]) / 2)

            if i == n-1:
                max_diff = max(max_diff,l - vet[i])

        print(max_diff)

if __name__ == "__main__":
    main()
