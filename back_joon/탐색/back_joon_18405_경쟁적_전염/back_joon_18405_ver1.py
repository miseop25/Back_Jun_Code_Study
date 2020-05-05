import sys
input = sys.stdin.readline


def spread(v_dic) :
    sort_v = sorted(v_dic.items(), key= lambda x: x[0])
    new_v = dict()
    dx = [0, 0 ,-1, 1]
    dy = [-1, 1, 0, 0]

    for location in sort_v :
        key = location[0]
        for tx, ty in location[1] :
            for i in range(4) :
                x = tx + dx[i]
                y = ty + dy[i]
                if x >=0 and x < N and y >= 0 and y < N :
                    if board[y][x] == 0 :
                        board[y][x] = key
                        if key in new_v :
                            new_v[key].append([x, y])
                        else :
                            new_v[key] = [ [x, y ] ]
    return new_v




N, K = map(int, input().split(" "))
board = []
virus = dict()
for i in range(N) :
    buf = list(map(int, input().split(" ")))
    board.append(buf)
    for j in range(N) :
        if buf[j] != 0 :
            if buf[j] in virus :
                virus[buf[j]].append([j, i])
            else :
                virus[buf[j]] = [[j, i]]

S , X , Y = map(int, input().split(" "))

for _ in range(S) :
    virus = spread(virus)

X -= 1
Y -= 1
if board[X][Y] == 0 :
    print(0)
else :
    print(board)
    print(board[X][Y])


