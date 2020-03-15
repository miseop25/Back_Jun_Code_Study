import sys
import collections
import copy
input = sys.stdin.readline



K = int(input())

def check_box(x,y) :
    try :
        if draw[x][y+1] == 1 and draw[x+1][y] == 1 and draw[x+1][y+1] == 1: 
            buf_box[x][y] = -1
            buf_box[x][y+1] = -1
            buf_box[x+1][y] = -1
            buf_box[x+1][y+1] = -1
    except :
        pass


for _ in range(K) :
    answer = True
    draw = []
    que = collections.deque([])
    N, M = map(int, input().split(" "))

    for i in range(N) :
        buf = list(map(int, input().split(" ")))
        for j in range(M) :
            if buf[j] == 1:
                que.append([i,j])
        draw.append(buf)
    buf_box = copy.deepcopy(draw)
    while que :
        x, y = que.popleft()
        check_box(x,y)

    for ch in buf_box :
        if 1 in ch :
            answer = False
            break

    if answer :
        print("YES")
    else :
        print("NO")

                    

    


