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
    t = inp()

    for _ in range(t):
        n,k = inlt()

        if k % 2 == 1:
            print("NO")
            continue
        else:


            vec = [0] * n
            j = n - 1

            for i in range(n - 1, (n - 1)//2, -1):

                if k == 0:
                    break

                x = 2 * j
                pos = min(x, k)


                vec[i  - pos // 2] = i + 1
                k -= pos
                j -= 2


            if k > 0:
                print("NO")
                continue
            else:
                print("YES")
                place = 1
                for i in range(n):
                    if vec[i] == 0:
                        vec[i] = place
                        place += 1

            print(" ".join(map(str, vec)))

if __name__ == "__main__":
    main()
