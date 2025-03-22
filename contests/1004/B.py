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
        n = inp()
        vet = inlt()

        vet.sort()

        countS = [0] * (n + 2)

        for i in vet:
            countS[i] += 1

        flag = True
        for i in range(1,n + 1):
            if countS[i] > 2:
                countS[i + 1] += countS[i] - 2
                countS[i] = 2

            if countS[i] % 2 == 1:
                flag = False

        if flag == True:
            print("yes")
        else:
            print("no")


if __name__ == "__main__":
    main()
