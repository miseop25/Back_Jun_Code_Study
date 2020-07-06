def find4Block(m, n ,board) :
    dx = [ 0, -1, -1]
    dy = [ -1, 0, -1]
    delBlock = set()
    for i in range(1, m) :
        for j in range(1, n) :
            flag = True
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
                    




def solution(m, n, board):
    answer = 0
    game = []
    for i in board :
        game.append(list(i))
    print(game)
    return answer
