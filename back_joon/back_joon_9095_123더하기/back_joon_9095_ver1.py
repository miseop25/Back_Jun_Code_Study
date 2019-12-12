def solution(num) :
    if num == 1 :
        return 1
    elif num == 2 :
        return 2
    elif num == 3 :
        return 4
    answer = 0
    ans_list = []
    buf_list = []
    number = [1,2,3]
    for i in number :
        check = 1 
        ans_list.append(i)
        while check == 1 :
            for j in ans_list :
                if (j+1) < num :
                    buf_list.append(j+1)
                elif (j+1) == num :
                        answer +=1 
                if (j+2) < num :
                    buf_list.append(j+2)
                elif (j+2) == num :
                    answer +=1
                
                if (j+3) < num :
                    buf_list.append(j+3)
                elif (j+3) == num :
                    answer +=1
            if buf_list :
                pass
            else :
                check = -1
            ans_list = buf_list
            buf_list = []
    return answer



N = int(input())

for i in range(N):
    num = int(input())
    print(solution(num))
