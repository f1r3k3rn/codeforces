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
        x,n,m = inlt()

        minx,maxx = int(1e10),0


        k = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))

        q = [(x,n,m)]

                if n1 + m1 == 0 or x1 == 0:
                    minx = min(minx,x1)
                    maxx = max(maxx,x1)
                    continue

                if n1 > 0:
                    q.append((x1//2,n1-1,m1))

                if m1 > 0:
                    if x1 != 1:
                        q.append((x1//2 + x1 % 2,n1,m1-1))
                    else:
                        q.append((1,n1,0))

        print(minx,maxx)

if __name__ == "__main__":
    main()
