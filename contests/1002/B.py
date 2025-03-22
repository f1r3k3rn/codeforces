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
        n,k = inlt()
        vet = inlt()

        s = 0
        k -= 1
        flag = False

        for i in range(1,n):
            if k == 0:
                break

            if flag:
                k -= 1
                flag = False
                continue

            if vet[i] == s + 1:
                k -= 1
                s += 1
                flag = True

        print(s + 1)


if __name__ == "__main__":
    main()
