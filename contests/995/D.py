import sys
import heapq
import bisect

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

def intersect(s1,s2):
    if s1[1] < s2[0] or s2[1] < s1[0]:
        return 0
    else:
        return min(s1[1],s2[1]) - max(s1[0],s2[0]) + 1

# WRITE HERE
def solve(n,x,y,vet):
    sol = 0
    decrement_l = [0] * n
    decrement_r = [0] * n

    ret = sorted(vet)
    s = sum(vet)

    for i in range(n):

        l = (x + vet[i] - s ) * -1
        r = (y + vet[i] - s) * -1

        l1 = bisect.bisect_right(ret,l) - 1
        r1 = bisect.bisect_left(ret,r)

        s1 = [0,l1]
        s2 = [r1,n]
        print(intersect(s1,s2))

        print(s1,s2)
        sol += intersect(s1,s2)

    return sol

# WRITE HERE

def main():
    t = inp()

    for _ in range(t):
        n,x,y = inlt()
        vet = inlt()
        print(solve(n,x,y,vet))



if __name__ == "__main__":
    main()
