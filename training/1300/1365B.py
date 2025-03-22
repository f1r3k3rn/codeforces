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
        vet = inlt()
        ret = inlt()

        flag = True

        for i in range(n):
            if ret[i] != ret[i - 1]:
                flag = False

        if flag:
            if vet == sorted(vet):
                print("Yes")
            else:
                print("No")
        else:
            print("Yes")


if __name__ == "__main__":
    main()
