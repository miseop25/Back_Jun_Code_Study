def solution(dirs):
    answer = 0
    board = [[0 for _ in range(11)]for _ in range(11)]
    x,y = 5,5
    board[y][x] = 1
    cmdDict = {"U" : 0, "D":1,"R":2, "L":3}
    dx = [0,0,1,-1]
    dy = [-1,1,0,0]

    k = dirs[0]
    index = cmdDict[k]

    if index >= 2 :
        answer = -1
    else :
        answer = 0

    for k in dirs :
        index = cmdDict[k]
        if x + dx[index] <0 or x + dx[index] > 10 or y + dy[index] < 0 or y + dy[index] > 10 :
            continue
        x += dx[index]
        y += dy[index]
        if x == 5 and y == 5 :
            answer -= 1
        if board[y][x] == 0 :
            board[y][x] = 1
    for i in board :
        answer += sum(i)

    return answer


print(solution("UUUDDD"))