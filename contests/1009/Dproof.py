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


def punti_nel_cerchio(r):
    centro_x, centro_y = 0, r  # Centro del cerchio in (0, r)
    s = 0

    for x in range(-r, r + 1):
        for y in range(-r, r + 1):
            if (x - centro_x) ** 2 + y ** 2 <= r ** 2:
                s += 1

    return s

def conta_quadrati_nel_rombo(r):
    count = 0

    for i in range(r):
        count += 2 * i + 1

    for i in range(r):
        count += 2 * i + 1

    count += 2 * r + 1
    return count

def main():
    t = inp()

    for _ in range(t):

        r = inp()
        print(punti_nel_cerchio(r))
        print(conta_quadrati_nel_rombo(r))



if __name__ == "__main__":
    main()
