def solution(n):
    answer = []
    maxNum = 1
    for i in range(2, n+1) :
        maxNum += i
    board = [[0 for _ in range(n)]for _ in range(n)]

    i,j = 0,0
    num = 1
    board[i][j] = num
    case = 1
    while num <= maxNum :
        board[i][j] = num
        num += 1
        if case == 1 :
            i += 1
            if i >= n : 
                case = 2
                i -= 1
                j += 1
            elif board[i][j] != 0 :
                case = 2
                i -= 1
                j += 1
        elif case == 2 :
            j += 1
            if j >= n :
                case = 3
                j -= 2
                i -= 1
            elif board[i][j] != 0 :
                case = 3
                i -= 1
                j -= 2
        elif case == 3 :
            i -= 1
            j -= 1
            if board[i][j] != 0 :
                case = 1
                i += 2
                j += 1
    for i in board :
        for j in i :
            if j != 0 :
                answer.append(j)
                

    return answer



print(solution(5))