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

def is_square(l, r, d, u):
    points = {(-l, 0), (r, 0), (0, -d), (0, u)}

    points = list(points)

    def distance_sq(p1, p2):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

    distances = []
    for i in range(4):
        for j in range(i + 1, 4):
            distances.append(distance_sq(points[i], points[j]))

    distances.sort()

    return (
            distances[0] > 0 and
            distances[0] == distances[1] == distances[2] == distances[3] and
            distances[4] == distances[5] and
            distances[4] == 2 * distances[0]
    )

def main():
    t = inp()

    for _ in range(t):
        l,r,d,u = inlt()

        if is_square(l, r, d, u):
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
