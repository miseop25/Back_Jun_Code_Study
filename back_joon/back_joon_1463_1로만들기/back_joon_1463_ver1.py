def soluction(N) :
    answer = 0
    buf_list = [N]
    check = [True for i in range(N+1)]
    while True :
        temp = []
        for i in buf_list :
            if i % 3 == 0 :
                case1 = i // 3
                if case1 == 1: 
                    return answer + 1
                if check[case1] :
                    check[case1] = False
                    temp.append(case1)
            if i % 2 == 0 :
                case2 = i // 2
                if case2 == 1 :
                    return answer + 1
                if check[case2] :
                    check[case2] = False
                    temp.append(case2)
            case3 = i -1
            if case3 == 1 :
                return answer + 1
            if check[case3] :
                check[case3] = False
                temp.append(case3)
        answer += 1
        buf_list = list(set(temp))
    return answer

N = int(input())
print(soluction(N))