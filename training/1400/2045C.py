import sys
import heapq
from collections import defaultdict
from sys import flags

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

    s,t = insr(),insr()

    t = t[:: - 1]

    visitedS = [1e9] * 27
    visitedT = [1e9] * 27

    sol = '-1'

    for i in range(1,len(s)):
        visitedS[ord(s[i]) - ord('a')] = min(visitedS[ord(s[i]) - ord('a')],i)

    for i in range(1,len(t)):
        visitedT[ord(t[i]) - ord('a')] = min(visitedT[ord(t[i]) - ord('a')],i)

    for i in range(27):

        if visitedT[i] != 1e9 and  visitedS[i] != 1e9:
            k = s[:visitedS[i] + 1] + t[:visitedT[i]][::-1]
            if len(sol) > len(k) or sol == '-1':
                sol = k

    print(''.join(sol))



if __name__ == "__main__":
    main()
