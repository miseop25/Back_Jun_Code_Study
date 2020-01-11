import sys
input=sys.stdin.readline
sys.setrecursionlimit(10000)

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

while True :
    w, h = map(int, input().split(' '))
    if w == 0 and h == 0 :
        break 

    island = []
    check = [[False]*w for _ in range(h)]
    for _ in range(h) :
        buf = list(map(int, input().split(' ')))
        island.append(buf)

    def dfs(x, y):
        check[x][y] = True
        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if island[nx][ny] == 1 and check[nx][ny] is False:
                dfs(nx, ny)

    #출처: https://rebas.kr/655 [PROJECT REBAS]    

    answer = 0
    for i in range(h) :
        for j in range(w) :
            if island[i][j] == 1 and check[i][j] is False :
                dfs(i,j)
                answer += 1

    print(answer)
    