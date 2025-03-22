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
        ans = vet[0]


        for i in range(1,n):
            ans += vet[i] - 1

        print(ans)






if __name__ == "__main__":
    main()
