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

        n,m = inlt()
        mat = [inlt() for _ in range(n)]
        sol = 0
        seen = [0] * (n * m + 1)

        for i in range(n):
            for j in range(m):

                if seen[mat[i][j]] == 0:
                    seen[mat[i][j]] = 1

                if seen[mat[i][j]] == 1:
                    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                        nx,ny = i+dx,j+dy
                        if 0 <= nx < n and 0 <= ny < m and mat[nx][ny] == mat[i][j] and seen[mat[i][j]] == 1:
                            seen[mat[i][j]] += 1

        print(sum(seen) - max(seen))





if __name__ == "__main__":
    main()
