from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y, cnt):
    q.append([x, y])
    a[x][y] = cnt
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny] == 0:
                    a[nx][ny] = cnt
                    q.append([nx, ny])

m, n, k = map(int, input().split())
a = [[0]*m for _ in range(n)]
c = a[:]
q = deque()
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            a[i][j] = -1

cnt = 1
for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            bfs(i, j, cnt)
            cnt += 1

cnt -= 1
print(cnt, end='\n')
ans = [0] * cnt
for i in range(n):
    for j in range(m):
        if a[i][j] > 0:
            ans[a[i][j]-1] += 1
ans.sort()
for i in range(len(ans)):
    print("{0} ".format(ans[i]), end='')