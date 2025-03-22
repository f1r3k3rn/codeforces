import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(10**5)

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
        n = inp()
        vet = inlt()

        root = 0
        paint = 0
        tree = [[] for i in range(n + 1)]
        solutions = [[] for i in range(n + 1)]


        for i in range(1, n + 1):
            if i != vet[i - 1]:
                tree[vet[i - 1]].append(i)
            else:
                root = i


        def lgbtq_dfs(node,color):

            nonlocal paint

            solutions[color].append(node)

            for i in range(len(tree[node])):
                if i != len(tree[node]) - 1:
                    paint += 1
                    lgbtq_dfs(tree[node][i], paint + 1)
                else:
                    lgbtq_dfs(tree[node][i],color)

        lgbtq_dfs(root,0)

        k = 0

        for i in range(n + 1):
            if len(solutions[i]) > 0:
                k += 1

        print(k)
        for sol in solutions:
            if len(sol) == 0:
                continue

            print(len(sol))
            print(" ".join(map(str,sol)))

        print()




if __name__ == "__main__":
    main()
