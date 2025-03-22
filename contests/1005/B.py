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


# WRITE HERE
def solve(n, vet):
    sol = 0

    counts = [0] * (n + 1)
    pfx = [0] * (n)

    for i in range(n):
        counts[vet[i]] += 1

    flag = False
    l,r = 0,0
    bl,br = 0,0
    for i in range(n):
        if counts[vet[i]] == 1:
            if sol < i - l + 1:
                sol = i - l + 1
                bl,br = l,i
            flag = True
        else:
            l,r = i+1,i+1


    if not flag:
        return 0


    return str(bl + 1) + " " + str(br + 1)


# WRITE HERE

def main():
    t = inp()

    for _ in range(t):
        n = inp()
        vet = inlt()
        print(solve(n, vet))


if __name__ == "__main__":
    main()
