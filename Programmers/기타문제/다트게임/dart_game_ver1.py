def solution(dartResult):
    answer = [0,0,0]
    score_list = []
    tmep = 0
    stack = []

    #  문자열을 3개로 나누는 작업 
    for i in range(1, len(dartResult) - 1 ) :
        if dartResult[i] >= "0" and dartResult[i] <= "9" :
            if stack :
                score_list.append(dartResult[tmep : i])
                tmep = i
                stack = []
        else :
            stack.append(dartResult[i])
    score_list.append(dartResult[tmep : ])

    # 나눈 문자열을 조건에 따라 점수를 부여하는 작업
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
        #  점수와 bonus는 항상 존재하지만 option은 없을 수도 있기 때문에 배열에 저장
        score = pow(int(num_buf), bonus)
        if option :
            #  option이 # 인 경우는 -1을 곱하고 *인 경우는 2를 본 점수와 이전 점수에 곱한다.
            if option[0] == -1 :
                score = score*-1
            else :
                if s > 0 :
                    answer[s-1] = answer[s-1]*2
                score *= 2
        answer[s] = score

    return sum(answer)

print(solution("1S2D*3T"))