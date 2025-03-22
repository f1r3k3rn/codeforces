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
    return sol


# WRITE HERE

def main():
    t = inp()

    for _ in range(t):
        n,m,k = inlt()
        questions = inlt()
        known = inlt()
        outs = []
        if len(known) < n - 1:
            outs.append("0" * m)
        elif len(known) == n:
            outs.append("1" * m)
        else:
            to_out = ""
            count_sort = [0] * (n + 1)
            for i in range(k):
                count_sort[known[i]] = 1

            only_not_known = 0

            for i in range(1, n + 1):
                if count_sort[i] == 0:
                    only_not_known = i
                    break

            for i in range(m):
                if questions[i] == only_not_known:
                    to_out += "1"
                else:
                    to_out += "0"

            outs.append(to_out)

        print("\n".join(outs))



if __name__ == "__main__":
    main()
