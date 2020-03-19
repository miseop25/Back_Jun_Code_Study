import sys
input = sys.stdin.readline

M, N, K = map(int, input().split(" "))

squre = [[1 for j in range(N)] for i in range(M)]
wall_list = []

for _ in range(K) :
    start_x, start_y , end_x, end_y = map(int, input().split(" "))
    for i in range(start_y, end_y) :
        for j in range(start_x, end_x) :
            squre[i][j] = 0


print(squre)


