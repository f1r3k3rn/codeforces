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
        a = inp()
        if a % 33 == 0:
            print("YES")
        else:
            a = str(a)
            flag = "NO"
            for i in range(len(a) - 1):

                if a[i] == a[i + 1] and a[i] == "3":
                    temp = a[:i] + a[i + 2:]
                    if int(temp) % 33 == 0:
                        flag = "YES"
                        break

            print(flag)


if __name__ == "__main__":
    main()
