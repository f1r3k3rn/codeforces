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
        s = insr()

        vet = [0] * 26

        for i in range(len(s)):
            vet[ord(s[i]) - 97] += 1

        f = True

        for i in range(26):
            if vet[i] % 2 != 0:
                f = False

        if f:
            print("First")
        else:
            if len(s) % 2 == 1:
                print("First")
            else:
                print("Second")




if __name__ == "__main__":
    main()
