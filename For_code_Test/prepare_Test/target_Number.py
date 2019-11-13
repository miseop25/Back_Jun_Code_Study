def do_plus_minus(ans_list, num) :
    buf_list =[]
    for i in ans_list :
        buf_list.append(i + num)
        buf_list.append(i - num)
    return buf_list


def solution(numbers, target):
    answer = 0
    ans_list = [0]
    for i in numbers :
        ans_list = do_plus_minus(ans_list, i)
    
    for k in ans_list :
        if k == target :
            answer += 1




    return answer