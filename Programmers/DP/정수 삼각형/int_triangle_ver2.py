def sum_cal(prelist, afterlist) :
    ans_list = []
    num = len(prelist)
    for i in range(num) :
        if i == 0 :
            ans_list.append(prelist[i] + afterlist[i])
        if i > 0 :
            first = prelist[i-1] + afterlist[i]
            second = prelist[i] + afterlist[i]
            ans_list.append(max(first, second))
        if i == num-1 :
            ans_list.append(prelist[i] + afterlist[i+1])
    return ans_list


def solution(triangle):
    answer = 0
    if len(triangle) == 1 :
        return triangle[0][0]
    else :
        ans_list = triangle[0]
        for i in range(1, len(triangle)) :
            ans_list = sum_cal(ans_list, triangle[i])
    answer = max(ans_list)
    return answer