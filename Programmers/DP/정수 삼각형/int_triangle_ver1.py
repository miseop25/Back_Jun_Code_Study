def sum_cal(prelist, afterlist) :
    ans_list = []
    num = len(prelist)
    for i in range(num) :
        if i == 0 :
            ans_list.append(prelist[i] + afterlist[i])
        if i >0 :
            first = prelist[i-1] + afterlist[i]
            second = prelist[i] + afterlist[i]
            if first > second :
                ans_list.append(first)
            else :
                ans_list.append(second)
        if i == num-1 :
            ans_list.append(prelist[i] + afterlist[i+1])
    return ans_list


def solution(triangle):
    answer = 0
    prelist = list()
    afterlist = list()

    for i in range(len(triangle)) : 
        if i == 0 :
            prelist = triangle[0]
            afterlist = prelist
        else :
            afterlist = triangle[i]
            prelist = sum_cal(prelist, afterlist)
    answer = max(prelist)
    
    return answer