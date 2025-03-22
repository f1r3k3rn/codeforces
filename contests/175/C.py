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


        n , k = inlt()
        s = insr()
        vet = inlt()


        l,r = 0, max(vet) + 1

        m = 0
        sol = 0
        while l < r:
            m = (l+r)//2


            taking = False
            possible = True
            x = 0

            for i in range(n):

                if vet[i] > m and s[i] == 'B' and taking == False:

                    if  x == k:
                        possible = False
                        break

                    x += 1
                    taking = True

                if taking == True and s[i] == 'R' and vet[i] > m:

                    taking = False

            if possible == True:
                sol = m
                r = m
            else:
                l = m + 1

        print(sol)


if __name__ == "__main__":
    main()
