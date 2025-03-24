import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline
from math import log2


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
        sol = 0
        vec = []

        if n % 2 == 1:
            vec.append(n)
            vec.append(n - 1)
            vec.append(3)
            vec.append(1)

            for i in range(1,n):
                if i != 1 and i != 3 and i != n - 1:
                    vec.append(i)
        else:
            vec.append(n)
            vec.append(2**int(log2(n)) - 1)
            vec.append(2**int(log2(n)) - 2)
            vec.append(5)
            vec.append(1)

            for i in range(1,n):
                if i != 1 and i != 5 and i != 2**int(log2(n)) - 1 and i != 2**int(log2(n)) - 2:
                    vec.append(i)

        vec = vec[::-1]

        for i in range(len(vec)):
            if i % 2 == 0:
                sol &= vec[i]
            else:
                sol |= vec[i]

        print(sol)

        print(' '.join(map(str,vec)))







if __name__ == "__main__":
    main()
