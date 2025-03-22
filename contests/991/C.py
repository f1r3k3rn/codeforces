import itertools
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
    digit_sum = 0
    three = 0
    twos = 0
    for i in range(len(s)):
        digit_sum += int(s[i])
        if s[i] == "3":
            three += 1
        if s[i] == "2":
            twos += 1


    digit_sum = digit_sum % 9

    if digit_sum == 0:
        return "YES"

    for i in range(three + 1):
        for j in range(twos + 1):
            if (6 * i + 2 * j + digit_sum ) % 9 == 0:
                return "YES"


    return "NO"


# WRITE HERE

def main():
    t = inp()

    for _ in range(t):
        s = insr()
        print(solve(s))


if __name__ == "__main__":
    main()
