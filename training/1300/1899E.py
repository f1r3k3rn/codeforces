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

    # array of n integers

    # he can apply the following operation any number of times:
    # rotation of first element
    # shifting it to the left until he becomes the greatest in the suffix

    for _ in range(t):
        n = inp()
        vet = inlt()

        k = min(vet)
        lastk = 0

        for i in range(n):
            if vet[i] == k:
                lastk = i
                break


        flag = True
        for i in range(lastk + 1, n):
            if vet[i] < vet[i - 1]:
                flag = False
                break

        if flag:
            print(lastk)
        else:
            print(-1)


if __name__ == "__main__":
    main()
