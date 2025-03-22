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

        sol = 0
        flag = False
        csort = [0] * n

        for i in range(n):
            csort[vet[i]] += 1

        for i in range(n):
            if csort[i] == 1:
                if flag:
                    break
                flag = True
            elif csort[i] == 0:
                break
            sol = i + 1

        print(sol)






if __name__ == "__main__":
    main()
