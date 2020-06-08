import sys
import collections
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    board = []
    answer = (N-2)**2
    dx = [-1, -1, -1, 0, 1, 1, 1, 0]
    dy = [-1, 0, 1, 1, 1, 0, -1, -1]

    for i in range(N) :
        temp = input().rstrip()
        board.append([])
        for j in range(N) :
            if temp[j] != "#" :
                board[i].append(int(temp[j]))
            else :
                board[i].append(-2)
    
    for i in range(1, N-1) :
        for j in range(1, N-1) :
            flag = False
            for k in range(8) :
                x = dx[k] + i
                y = dy[k] + j

                if board[x][y] == -2 : 
                    continue
                elif board[x][y] == 0 :
                    flag = True
                
            if flag :
                answer -= 1
            else :
                for k in range(8) :
                    x = i +dx[k]
                    y = j + dy[k]
                    if board[x][y] == -2 or board[x][y] == 0 :
                        continue

                    board[x][y] -= 1
    if N <= 2 :
        print(0)
    else :
        print(answer)