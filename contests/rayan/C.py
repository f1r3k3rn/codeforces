import sys
import heapq
from collections import defaultdict
from pydoc import visiblename

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


move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
directions = ['R', 'L', 'D', 'U']

# WRITE HERE
def solve(n,m,mat):
    sol = 0

    visited = [[0 for _ in range(m)] for _ in range(n)]


    for i in range(n):
        for j in range(m):
            if mat[i][j] != "?" and visited[i][j] == 0:
                length = 0
                visited[i][j] = 1
                q = [(i,j)]
                while q:
                    x,y = q.pop()
                    dx,dy = directions[move.index(mat[x][y])]

                    if mat[dx][dy] == "?":
                        visited[dx][dy] = 1
                        q.append((dx,dy))




                sol += 1


    return sol


# WRITE HERE
def main():
    t = inp()

    for _ in range(t):
        n,m = inlt()
        mat = [inlt() for _ in range(n)]
        solve(n, mat)


if __name__ == "__main__":
    main()
