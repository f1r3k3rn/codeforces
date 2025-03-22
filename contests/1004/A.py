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
def s(x):

    sol = 0

    while x > 0:
        sol += x % 10
        x = x // 10

    return sol


# WRITE HERE

def main():
    t = inp()

    for _ in range(t):
        vet = inlt()

        flag = False

        k = 1

        if vet[0] == vet[1] - 1:
            flag = True
        else:
            while True:

                if vet[0] - (k * 9 - 1) == vet[1]:
                    flag = True
                    break

                k += 1
                if vet[0] - (k * 9 - 1) < 0:
                    break

        if flag:
            print("yes")
        else:
            print("no")







if __name__ == "__main__":
    main()
