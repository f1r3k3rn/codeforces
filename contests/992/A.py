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
def solve(n,k, vet):

    sol  = ""
    z = 0

    for i in range(n):
        sol = "NO"

        for j in range(n):
            if i != j and abs(vet[i] - vet[j]) % k == 0:
                sol = "YES"
                break

        if sol == "NO":
            k = i + 1
            break

    if sol == "NO":
        return "YES" + "\n" + str(k)
    else:
        return "NO"


# WRITE HERE

def main():
    t = inp()

    for _ in range(t):
        n,k = inlt()
        vet = inlt()
        print(solve(n,k, vet))


if __name__ == "__main__":
    main()
