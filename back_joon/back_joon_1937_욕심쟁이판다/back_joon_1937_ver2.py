import sys
input = sys.stdin.readline
sys.setrecursionlimit(40000)
#  파이썬은 기본적으로 많은 재귀를 허용하지 않기 때문에 위 라인을 입력해 주어야 한다.

#  상 하 좌 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def soluction(x, y) :
    result_list = [1]
    temp = forest[y][x]
    for i in range(4) :
        answer = 1
        lx = x + dx[i]
        ly = y + dy[i]
        if lx >= 0 and lx < N and ly >= 0 and ly < N :
            if temp < forest[ly][lx] :
                if bfs[ly][lx] == 0 :
                    answer += soluction(lx, ly)
                else :
                    answer += bfs[ly][lx]
                result_list.append(answer)
    bfs[y][x] = max(result_list)
    return bfs[y][x]
 

N = int(input())
forest = []
bfs = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(N) :
    buf = list(map(int, input().split(" ")))
    forest.append(buf)

ans_list = [1]
for i in range(N) :
    for j in range(N) :
        check = soluction(j, i)
        ans_list.append(check)
print(max(ans_list))

