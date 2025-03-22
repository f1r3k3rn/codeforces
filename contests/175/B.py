import sys
import heapq
from collections import defaultdict
from time import sleep

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
        n, x, sec = inlt()

        mov = insr()


        t = 0
        sol = 0
        i = 0
        flag = False
        rflag = False

        while i < len(mov):

            if mov[i] == "R":
                x += 1
            else:
                x -= 1

            t += 1
            i += 1

            if x == 0:
                if flag == False:
                    sol += 1
                    i = 0
                    flag = True
                else:
                    rflag = True
                    sol += 1
                    break


        if rflag == True:
            sol += (sec - t) // i

        print(sol)


if __name__ == "__main__":
    main()
