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
        n,x,y = inlt()
        vet = inlt()

        vet.sort()

        # per ogni elemnto devo capire quanti elementi sono uguali a lui mod y e quanti sono uguali al suo negativo mod x

        r = defaultdict(lambda: defaultdict(int))

        for i in range(n):
            r[vet[i] % x][vet[i] % y] += 1

        sol = 0
        for i in range(n):

            r[(vet[i]) % x][vet[i] % y] -= 1
            sol += r[(-vet[i]) % x][vet[i] % y]

        print(sol)

if __name__ == "__main__":
    main()
