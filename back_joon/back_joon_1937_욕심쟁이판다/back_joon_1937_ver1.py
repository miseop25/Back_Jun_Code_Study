import sys
input = sys.stdin.readline


def soluction(x, y) :
    #  상 하 좌 우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    result_list = [1]
    temp = forest[y][x]
    for i in range(4) :
        answer = 1
        if x + dx[i] >= 0 and x + dx[i] < N and y + dy[i] >= 0 and y + dy[i] < N :
            if temp < forest[y + dy[i]][x + dx[i]] :
                answer += soluction(x + dx[i], y + dy[i])
                result_list.append(answer)
    return max(result_list)

N = int(input())
forest = []
for _ in range(N) :
    buf = list(map(int, input().split(" ")))
    forest.append(buf)

ans_list = [1]
for i in range(N) :
    for j in range(N) :
        ans_list.append(soluction(j,i))
print(max(ans_list))

