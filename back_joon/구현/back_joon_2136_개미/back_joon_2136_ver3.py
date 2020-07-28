import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N, L = map(int, (input().split(" ")))
    ant = []

    for i in range(1, N+1) :
        buf = int(input())
        ant.append([buf, i])
    ant = sorted(ant, key= lambda x: abs(x[0]))


