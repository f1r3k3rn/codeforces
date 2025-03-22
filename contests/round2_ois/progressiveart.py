import sys
import heapq
from collections import defaultdict
from operator import truediv

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
    return sol


# WRITE HERE

def main():
    N,M,L,K = inlt()
    s = 0
    mat = [["" for i in range(M)] for i in range(N)]

    if (N - L + 1) * (M - L + 1) < K or (L * L) % 3 != 0 and K != 0:
        print("NO")
        return
    else:
        print("YES")

        for i in range(N):
            for j in range(M):
                if j % 3 == 0:
                    mat[i][j] = "R"
                elif j % 3 == 1:
                    mat[i][j] = "G"
                else:
                    mat[i][j] = "B"

        s = (N - L + 1) * (M - L + 1)

        for i in range(N - L + 1):
            for j in range(M - L + 1):
                if s == K:
                    break
                else:
                    if j % 3 == 0:
                        mat[i][j] = "B"
                        if j > 0:
                            mat[i][j - 1] = "B"
                    if j % 3 == 1:
                        mat[i][j] = "B"
                    if j % 3 == 2:
                        mat[i][j] = "R"

                    s -= 1

            if s == K:
                break

            for k in range(M):
                mat[i][k] = "B"
        """
        perfect = 0

        for i in range(N - L + 1):
            for j in range(M - L + 1):
                r,g,b = 0,0,0
                for k in range(L):
                    for q in range(L):
                        if mat[i + k][j + q] == "R":
                            r += 1
                        elif mat[i + k][j + q] == "G":
                            g += 1
                        else:
                            b += 1
                if r == g and r == b:
                    perfect += 1

        print(perfect)
        """
        for i in range(N):
            print("".join(mat[i]))



if __name__ == "__main__":
    main()