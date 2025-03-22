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
def solve(n):
    sss = "aeiou"
    vet = [0] * 5
    k = n // 5
    s = n % 5
    out = ""

    for i in range(5):
        vet[i] += k

    for i in range(s):
        vet[i] += 1

    for i in range(5):
        out += sss[i] * vet[i]

    return out


# WRITE HERE

def main():
    t = inp()

    for _ in range(t):
        n = inp()
        print(solve(n))


if __name__ == "__main__":
    main()
