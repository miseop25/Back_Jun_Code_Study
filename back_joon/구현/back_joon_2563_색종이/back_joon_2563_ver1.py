import sys
import collections
input = sys.stdin.readline

N = int(input())
answer = N*100

que = collections.deque([])

for i in range(N):
    x,y  = map(int, input().split(" "))
    x2 = x + 10
    y2 = y + 10
    que.append([x,x2,y,y2])

while que :
    x , x2 , y, y2 = que.popleft()
    for i in que :
        check_x = abs(x - i[0]) + abs(x2- i[1])
        check_y = abs(y -i[2]) + abs(y2-i[3])
        if check_x <= 18 and check_y <= 18 :
            answer -= (10 -check_x//2)*(10 -check_y//2)

print(answer)
