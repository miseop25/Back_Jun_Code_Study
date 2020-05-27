import sys
input = sys.stdin.readline

def checkCangedBlock(x, y) :
    first = 0
    last = 0
    ch1 = board[x][y]
    if ch1 == "B" :
        ch2 = "W"
    else :
        ch2 = "B"
    
    for i in range(8) :
        for j in range(8) :
            if i%2 == 0 :
                if j%2 == 0 :
                    if board[x+ i][y+j] != ch1 :
                        first += 1
                    if board[x+ i][y+j] != ch2 :
                        last += 1
                else :
                    if board[x+ i][y+j] == ch1 :
                        first += 1
                    if board[x+ i][y+j] == ch2 :
                        last += 1
            else :
                if j%2 == 0 :
                    if board[x+ i][y+j] == ch1 :
                        first += 1
                    if board[x+ i][y+j] == ch2 :
                        last += 1
                else :
                    if board[x+ i][y+j] != ch1 :
                        first += 1
                    if board[x+ i][y+j] != ch2 :
                        last += 1
    return min(first, last)



if __name__ == "__main__":
    answer = []
    board = []
    N, M = map(int, input().split(" "))
    for _ in range(N) :
        board.append(input().rstrip())
    
    for i in range(N -7) :
        for j in range(M-7) :
            answer.append(checkCangedBlock(i, j))
    print(min(answer))




