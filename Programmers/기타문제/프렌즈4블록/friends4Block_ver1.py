def find4Block(m, n ,board) :
    dx = [ 0, -1, -1]
    dy = [ -1, 0, -1]
    delBlock = set()
    for i in range(1, m) :
        for j in range(1, n) :
            flag = True
            if board[i][j] == "X" : continue
            comp = board[i][j]
            for k in range(3) :
                x = i + dx[k]
                y = j + dy[k]
                if board[x][y] != comp :
                    flag = False
                    break
            if flag :
                delBlock.add((i,j))
                for k in range(3) :
                    x = i + dx[k]
                    y = j + dy[k]
                    delBlock.add((x, y))
    if len(delBlock) == 0 :
        return False
    return delBlock

def blockDown(m,n, board) :
    for i in range(m-1) :
        for j in range(n) :
            if board[i+1][j] == "X" and board[i][j] != "X" :
                temp = []
                for t in range(i, -1, -1) :
                    if board[t][j] != "X" :
                        temp.append(board[t][j])
                        board[t][j] = "X"
                    else :
                        break
                board[i][j] = "X"
                for k in range(i+1, m) :
                    if board[k][j] != "X" :
                        for t in range(k - len(temp), k ) :
                            board[t][j] = temp.pop()

                        break
                    else :
                        board[k][j] = "X"
                if temp :
                    for t in range(m- len(temp), m) :
                        board[t][j] = temp.pop()
                
    return board
    
def delectBlock(d, board) :
    for x, y in d :
        board[x][y] = "X"
    return board





def solution(m, n, board):
    answer = 0
    game = []
    for i in board :
        game.append(list(i))

    delList = find4Block(m,n,game)
    if delList != False :
        answer += len(delList)
    while delList :
        game = delectBlock(delList, game)
        game = blockDown(m,n, game)
        delList = find4Block(m,n,game)
        if delList != False :
            answer += len(delList)
    return answer


print(solution(4,4,["ABCD", "BACE", "BCDD", "BCDD"] ))
