def solution(v):
    answer = []
    x_point = []
    y_point = []
    for i in v :
        x_point.append(i[0])
        y_point.append(i[1])
    
    x_1 = x_point[0]
    y_1 = y_point[0]
    for i in x_point :
        if x_1 != i :
            x_2 = i
    
    for i in y_point :
        if y_1 != i :
            y_2 = i

    if x_point.count(x_1) == 1 :
        answer.append(x_1)
    else :
        answer.append(x_2)
    
    if y_point.count(y_1) == 1 :
        answer.append(y_1)
    else :
        answer.append(y_2)

    print(answer)
    return answer