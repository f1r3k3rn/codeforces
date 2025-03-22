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



def isperfectsquare(x):
    s = int(x ** 0.5)
    return s * s == x

# WRITE HERE

def main():
    t = inp()

    for _ in range(0,t):
        n = inp()

        if n == 1 or isperfectsquare(n * (n + 1) // 2):
            print(-1)
        else:
            k = [i for i in range(1, n + 1)]


            for i in range(0, n - 1):

                if isperfectsquare((i + 1) * (i + 2) // 2) == True:
                    k[i], k[i + 1] = k[i + 1], k[i]


            print(" ".join(map(str, k)))

if __name__ == "__main__":
    main()
