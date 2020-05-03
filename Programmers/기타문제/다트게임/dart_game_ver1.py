def solution(dartResult):
    answer = [0,0,0]
    score_list = []
    tmep = 0
    stack = []
    for i in range(1, len(dartResult) - 1 ) :
        if dartResult[i] >= "0" and dartResult[i] <= "9" :
            if stack :
                score_list.append(dartResult[tmep : i])
                tmep = i
                stack = []
        else :
            stack.append(dartResult[i])
        

    score_list.append(dartResult[tmep : ])
    print(score_list)

    for s in range(3) :
        num_buf = ''
        bonus = 0
        option = []
        for i in score_list[s] :
            if i >= '0' and i <= '9' :
                num_buf += i
            elif i == "S" :
                bonus = 1
            elif i == "D" :
                bonus = 2
            elif i == "T" :
                bonus = 3
            elif i == "#" :
                option.append(-1)
            elif i == "*" :
                option.append(2)

        score = pow(int(num_buf), bonus)
        if option :
            if option[0] == -1 :
                score = score*-1
            else :
                if s > 0 :
                    answer[s-1] = answer[s-1]*2
                score *= 2
        answer[s] = score

    return sum(answer)

print(solution("1S2D*3T"))