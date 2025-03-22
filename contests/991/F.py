import sys
import heapq
from collections import defaultdict
from math import gcd, log2, floor

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

class SparseTableGCD:
    def __init__(self, array):
        self.array = array
        self.n = len(array)
        self.k = floor(log2(self.n)) + 1
        self.sparse = [[0] * self.k for _ in range(self.n)]
        self.build_sparse_table()

    def build_sparse_table(self):
        for i in range(self.n):
            self.sparse[i][0] = self.array[i]

        j = 1
        while (1 << j) <= self.n:
            i = 0
            while (i + (1 << j) - 1) < self.n:
                self.sparse[i][j] = gcd(
                    self.sparse[i][j-1],
                    self.sparse[i + (1 << (j-1))][j-1]
                )
                i += 1
            j += 1

    def query(self, left, right):
        length = right - left + 1
        j = floor(log2(length))
        return gcd(
            self.sparse[left][j],
            self.sparse[right - (1 << j) + 1][j]
        )


# WRITE HERE
def solve(n, q, vet):

    ret = [abs(vet[i] - vet[i + 1]) for i in range(n - 1)]
    if n > 1:
        st = SparseTableGCD(ret)
    out = []
    for _ in range(q):
        l, r = inlt()
        l -= 1
        r -= 1
        if l == r:
            out.append(0)
        else:
            out.append(st.query(l, r - 1))


    return " ".join(map(str, out))


# WRITE HERE




def main():
    t = inp()

    for _ in range(t):
        n,q = inlt()
        vet = inlt()
        print(solve(n, q, vet))


if __name__ == "__main__":
    main()
