import sys
input = sys.stdin.readline


def soluction() :
    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]

    I = int(input())
    board = [[0 for _ in range(I)] for _ in range(I)]
    st_x, st_y = map(int, input().split(" "))
    ed_x , ed_y = map(int, input().split(" "))
    if st_x == ed_x and st_y == ed_y :
        return 0
    board[st_y][st_x] = 0
    bfs =[[st_y, st_x]]
    while True :
        buf = []
        for y, x in bfs :
            for i in range(8) :
                if x + dx[i] >= 0 and x + dx[i] < I and y + dy[i] >= 0 and y + dy[i] < I :
                    tx = x + dx[i]
                    ty = y + dy[i] 
                    if board[ty][tx] == 0 :
                        board[ty][tx] = board[y][x] + 1
                        buf.append([ty, tx])
                    if tx == ed_x and ty == ed_y :
                        return board[ed_y][ed_x]
        bfs = buf
    
                    





T = int(input())
for _ in range(T) :
    print(soluction())