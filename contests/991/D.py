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
def solve(vet):

    sol = ""
    n = len(vet)
    for i in range(n):
        mas = 0
        k = 0
        for j in range(1, 9):
            if i + j < n:
                if int(vet[i + j]) - j > mas:
                    k = i + j
                mas = max(int(vet[i + j]) - j, mas)

        if mas > int(vet[i]):
            vet = vet[:i] + [mas] + [vet[i]] + vet[i + 1:k] + vet[k + 1:]

    return "".join(map(str, vet))


# WRITE HERE

def main():
    t = inp()
    outs = []
    for _ in range(t):
        s = insr()
        outs.append(solve(s))

    print("\n".join(outs))


if __name__ == "__main__":
    main()
