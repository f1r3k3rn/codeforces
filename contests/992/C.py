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
def solve(n, k):
    sol = -1
    permz = [[(i + 1) for i in range(n)][:-2]]
    pairs = [[n, n - 1], [n - 1, n]]

    for i in pairs:
        for j in range(n - 1):
            permz.append(permz[0][:j] + i + permz[0][j:])

            if len(permz) > 3 and j + 3 < n:
                temp = permz[-1]
                temp[j], temp[j + 3] = temp[j + 3], temp[j]
                permz.append(temp)

    permz = permz[1:]
    permz = sorted(permz)
    print(permz)
    if k <= len(permz):
        sol = " ".join(map(str,permz[k - 1]))

    return sol


# WRITE HERE

def main():
    t = inp()

    for _ in range(t):
        n,k = inlt()
        print(solve(n,k))


if __name__ == "__main__":
    main()
