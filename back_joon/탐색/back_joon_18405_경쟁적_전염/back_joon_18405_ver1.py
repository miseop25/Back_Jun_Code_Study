import sys
input = sys.stdin.readline


def spread(v_dic) :
    #  바이러스를 낮은 번호 순대로 정렬한다.
    sort_v = sorted(v_dic.items(), key= lambda x: x[0])
    new_v = dict()
    #  상하 좌우 4방향
    dx = [0, 0 ,-1, 1]
    dy = [-1, 1, 0, 0]

    for location in sort_v :
        key = location[0]
        for tx, ty in location[1] :
            for i in range(4) :
                x = tx + dx[i]
                y = ty + dy[i]
                if x >=0 and x < N and y >= 0 and y < N :
                    #  해당 칸이 0일때만 바이러스가 채워진다. 마찬가지로 dict에 저장
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
        #  바이러스가 존재하는 경우 dict에 키는 바이러스 번호, Value는 위치를 저장
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
    print(board[X][Y])


