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


def main():
    t = 1

    for _ in range(t):
        n,k = inlt()
        vet = inlt()

        sliding_window = sum(vet[:k])

        min_sum = sliding_window
        min_sum_index = 0

        for i in range(1, n - k + 1):
            sliding_window = sliding_window - vet[i - 1] + vet[i + k - 1]
            if sliding_window < min_sum:
                min_sum = sliding_window
                min_sum_index = i

        print(min_sum_index + 1)



if __name__ == "__main__":
    main()
