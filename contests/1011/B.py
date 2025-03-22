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


        if k > 1:
            vet.sort(reverse=True)
            sol = sum(vet[:k]) + vet[k]
        else:
            mas = 0

            for i in range(n):
                if i == 0:
                    mas = max(mas, vet[i] + vet[n - 1])
                elif i == n - 1:
                    mas = max(mas, vet[i] + vet[0])
                else:
                    mas = max(vet[i] + max(vet[n - 1], vet[0]), mas)

            sol = mas

        print(sol)




if __name__ == "__main__":
    main()
