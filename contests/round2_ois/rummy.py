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
def solve(n, graph):
    distance_root = [10**6] * n
    distance_leaf = [10**6] * n

    s = [0]
    distance_root[0] = 0
    while len(s) > 0:
        node = s.pop()
        for i in graph[node]:
            if distance_root[i] > distance_root[node] + 1:
                distance_root[i] = distance_root[node] + 1
                s.append(i)

    s = [n - 1]
    distance_leaf[n - 1] = 0
    while len(s) > 0:
        node = s.pop()
        for i in graph[node]:
            if distance_leaf[i] > distance_leaf[node] + 1:
                distance_leaf[i] = distance_leaf[node] + 1
                s.append(i)


    count_sort = [0] * (n + 1)

    for i in range(n):
        count_sort[distance_leaf[i]] += 1

    for i in range(1,n):
        count_sort[i] += count_sort[i-1]

    print(count_sort)
    sol = 0
    for i in range(n):
        k = distance_root[n - 1] - distance_root[i] - 2
        print(i,k)

        if k < 0:
            sol += n - 1
        else:
            sol += n - 1 - count_sort[k]

        for j in graph[i]:
            if distance_leaf[j] <= k:
                sol -= 2
            else:
                sol -= 1

    return  sol



def main():
    n , m = inlt()
    graph = [[] for i in range(n)]
    for _ in range(m):
        to,a = inlt()
        graph[to].append(a)
        graph[a].append(to)

    print(solve(n, graph))


if __name__ == "__main__":
    main()
