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
        sol = 0
        i = 0
        while n > 0:
            r = n % 10

            if r > 4 and n != 9:
                sol += (9 - r) * pow(10,i)
            else:
                sol += r * pow(10,i)

            n //= 10
            i += 1

        print(str(sol))


if __name__ == "__main__":
    main()
