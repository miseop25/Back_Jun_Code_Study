import collections
def solution(board):
    answer = [1]
    zero_point = []
    for i in range(len(board)) :
        for j in range(len(board[0])) :
            if board[i][j] == 0 :
                zero_point.append([i, j])
    width = len(board[0])
    hight = len(board)
    zero_point = collections.deque(zero_point)
    while zero_point :
        y, x = map(int, zero_point.popleft())
        new_w = 0
        new_h = 0
        check = True
        if y < hight-1 and x < width-1 :
            if zero_point[0][0] != y :
                new_w = width - x - 1
                for find in zero_point :
                    if find[1] == (x+1) :
                        new_h = find[0] - y 
                        check = False
                        break   
                if check :
                    new_h = hight - y - 1
            else :
                new_w = zero_point[0][1] - x - 1
                for find in zero_point :
                    if find[1] == (x+1) :
                        new_h = find[0] - y 
                        check = False
                        break   
                if check :
                    new_h = hight - y - 1
            if new_w == new_h :
                answer.append(new_h*new_w)
    return max(answer)

print(solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))