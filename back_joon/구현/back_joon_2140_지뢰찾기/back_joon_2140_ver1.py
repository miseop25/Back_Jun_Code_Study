import sys
import collections
input = sys.stdin.readline

def changeMine(x,y , count) :
    global answer
    dx = [-1, -1, -1, 0, 1, 1, 1, 0]
    dy = [-1, 0, 1, 1, 1, 0, -1, -1]
    cnt = count
    for i in range(8) :
        tx = dx[i] + x
        ty = dy[i] + y
        if tx > 0 and tx < N-1 and ty > 0 and ty < N-1 :
            if board[tx][ty] == -1 :
                cnt -= 1
            elif board[tx][ty] == 0 and cnt != 0:
                board[tx][ty] = -1
                cnt -= 1
            elif board[tx][ty] != 1 and cnt == 0 :
                board[tx][ty] = 1
                answer -= 1
                
if __name__ == "__main__":
    N = int(input())
    board = []
    mine = dict()
    answer = (N-2)**2
    for i in range(4) :
        mine[i] = collections.deque([])

    for i in range(N) :
        temp = input().rstrip()
        board.append([])
        for j in range(N) :
            if temp[j] != "#" :
                mine[int(temp[j])].append(collections.deque([i, j]))
                board[i].append(temp[j])
            else :
                board[i].append(0)
    
    for i, j in mine[0] :
        changeMine(i,j, 0)
    for key in range(3, 0, -1) :
        for i, j in mine[key] :
            changeMine(i, j, key)
    if N <= 2 :
        print(0)
    else :
        print(answer)