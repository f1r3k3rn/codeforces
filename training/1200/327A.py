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
        n = inp()
        vet = inlt()

        sol = 0

        for i in range(n):
            zero = 0
            one = 0

            for j in range(i,n):
                if vet[j] == 0:
                    zero += 1
                else:
                    one += 1
                sol = max(sol,sum(vet) - one + zero)

        print(sol)



if __name__ == "__main__":
    main()
