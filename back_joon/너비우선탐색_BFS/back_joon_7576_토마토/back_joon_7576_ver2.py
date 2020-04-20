import sys
import collections
input = sys.stdin.readline


def update_tomato(update_list, tomato) :
    for i in update_list :
        tomato[i[0]][i[1]] = 1
    return tomato

def check_tomato_BFS(tomato, M , N) :
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]

    day = -1

    while que :
        day += 1
        for _ in range(len(que)) :
            x, y = que.popleft()

            for i in range(4) :
                nx = x + dx[i]
                ny = y + dy[i]

                if (0<= nx < N) and (0<= ny < M) and (tomato[nx][ny] == 0) :
                    tomato[nx][ny] = 1
                    que.append([nx, ny])
            
    
    for c in tomato :
        if 0 in c :
            return -1
    return day


M ,N = map(int, input().split(" "))
tomato , que = [], collections.deque()
day = 0
for i in range(N) :
    buf = list(map(int, input().split(" ")))
    for j in range(M) :
        if buf[j] == 1 :
            que.append([i,j])
    tomato.append(buf)

answer = check_tomato_BFS(tomato, M, N)
print(answer)
