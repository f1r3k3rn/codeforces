import sys
import heapq
from collections import defaultdict
import  random

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
        n = inp()

        sol = [1,2,3]
        for i in range(75):

            print(f"? {sol[0]} {sol[1]} {sol[2]}\n",flush=True)

            answ = inp()

            if answ == 0:
                break
            else:

                k = random.randint(0,3)

                if k == 0:
                    sol[0] = answ
                elif k == 1:
                    sol[1] = answ
                else:
                    sol[2] = answ

        print(f"! {sol[0]} {sol[1]} {sol[2]}\n",flush=True)



if __name__ == "__main__":
    main()
