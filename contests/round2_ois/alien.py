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
def solve(s):

    sol = 0
    v = set()
    r = []
    f = 0
    skip = 0

    for i in range(len(s)):
        if skip == 1:
            skip = 0
            continue
        if i < len(s) - 1:
            if s[i] == s[i + 1]:
                if s[i]*2 not in v:
                    v.add(s[i]*2)
                    r.append(s[i]*2)
                    skip = 1
                else:
                    f = -1
                    break
            else:
                if s[i] not in v:
                    v.add(s[i])
                    r.append(s[i])
                else:
                    f = -1
                    break
        else:
            if s[i] not in v:
                v.add(s[i])
                r.append(s[i])
            else:
                f = -1
                break

    if f == -1:
        return -1
    else:
        return " ".join(r)


# WRITE HERE

def main():
    t = inp()

    for _ in range(t):
        s = insr()
        print(solve(s))


if __name__ == "__main__":
    main()
