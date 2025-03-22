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
    return sol


# WRITE HERE

def main():
    t = inp()

    for _ in range(t):
        a = input()[:-1]
        n = len(a)

        xor1 = int(a,2)
        mas = xor1
        l,r = 0,0
        for i in range(n):
            if a[i] == "0":
                for j in range(n):
                    if a[j] == "1" and j + n - i <= n:
                        x = int(a[j:j + n - i],2)
                        if mas < xor1 ^ x:
                            mas = xor1 ^ x
                            l,r = j + 1,j + n - i
            if l != 0:
                break

        if l == 0:
            print(1,n,n,n)
        else:
            print(1,n,l,r)


if __name__ == "__main__":
    main()
