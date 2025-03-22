import sys
import heapq
from collections import defaultdict
from bisect import bisect_left, bisect_right

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
        n,m = inlt()
        a = inlt()

        coefficients = [0] * (n + 2)
        coefficients[0] = m

        for i in range(m):
            coefficients[a[i] + 1] += -1

        for i in range(1, n + 1):
            coefficients[i] += coefficients[i - 1]


        sol = 0

        for i in range(1,n//2 + 1):

            sol += (coefficients[i] * coefficients[n - i] - coefficients[n - i]) * (1 if n % i == 0 and n // i == 2 else 2)

        print(sol)

if __name__ == "__main__":
    main()
