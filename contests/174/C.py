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
    flag = 0


    l,r = 0,0
    ml,mr = 0,0
    s = set()

    for i in range(n):
        if vet[i] == 1 or vet[i] == -1:
            l += vet[i]
            l = max(l,0)
            ml = max(ml,l)

            r += vet[i]
            r = min(r,0)
            mr = min(mr,r)
        else:
            flag = i
            l,r = 0,0
            continue

    x1,x2 = 0,0
    y1,y2 = 0,0

    z = 0
    for i in range(flag + 1,n):
        z += vet[i]
        x1 = max(x1,z)
        y1 = min(y1,z)

    z = 0
    for i in range(flag - 1,-1,-1):
        z += vet[i]
        x2 = max(x2,z)
        y2 = min(y2,z)

    for i in range(mr,ml + 1):
        s.add(i)

    for i in range(min(y1 + y2,min(y1,y2)),max(x2 + x1,max(x1,x2)) + 1):
        s.add(i + vet[flag])

    z = [i for i in s]
    z.sort()

    return str(len(z)) + "\n" + " ".join(map(str,z))


# WRITE HERE

def main():
    t = inp()

    for _ in range(t):
        n = inp()
        vet = inlt()
        print(solve(n, vet))


if __name__ == "__main__":
    main()
