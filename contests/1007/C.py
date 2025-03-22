import sys
import heapq
from collections import defaultdict
from copyreg import dispatch_table

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
    t = inp()

    for _ in range(t):
        n,st,e = inlt()

        graph = [[] for _ in range(n+1)]

        for i in range(n - 1):
            u,v = inlt()
            graph[u].append(v)
            graph[v].append(u)

        to_order = []
        visited = [False] * (n+1)

        q = [(e,0)]

        while q:
            node, dist = q.pop(0)
            visited[node] = True
            to_order.append((node,dist))

            for adj in graph[node]:
                if visited[adj] == False:
                    q.append((adj,dist+1))

        to_order.sort(key=lambda x: x[1], reverse=True)
        to_out = [x[0] for x in to_order]

        print(*to_out)





if __name__ == "__main__":
    main()
