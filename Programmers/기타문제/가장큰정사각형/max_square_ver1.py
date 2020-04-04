def solution(board):
    answer = [1]
    st_point = []
    end_point = []
    check = 0
    for i in range(len(board)) :
        for j in range(len(board[0])) :
            if check == 0 :
                if board[i][j] == 1 :
                    check = 1
                    st_point.append([i,j])
            else :
                if board[i][j] == 0 :
                    check = 0
                    end_point.append([i,j-1])
        if check == 1 :
            end_point.append([i, j])
            check = 0

    for a in range(len(st_point)):
        st = st_point[a]
        ed = end_point[a]
        width = ed[1] - st[1] + 1
        
        for j in range(st[1] , ed[1]+1):
            heigth = 0
            for i in range(st[0], len(board)) :
                if board[i][j] == 1 :
                    heigth += 1
                else :
                    if width != heigth :
                        width = heigth
                    break
        answer.append(width*heigth)

    return max(answer)

print(solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))