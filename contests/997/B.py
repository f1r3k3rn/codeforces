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
    t = inp()

    for _ in range(t):
        n = inp()

        sol = [0] * n

        for i in range(n):
            s = input().strip()[i + 1:].count("0")

            for j in range(n):
                if sol[j] == 0 and s == 0:
                    sol[j] = i + 1
                    break
                elif sol[j] == 0:
                    s -= 1


        print(" ".join(map(str, sol)))


if __name__ == "__main__":
    main()
