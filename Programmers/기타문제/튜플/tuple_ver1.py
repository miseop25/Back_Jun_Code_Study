def solution(s):
    answer = []
    num_list = []
    buf = ""
    index = 0

    #  처리하기 쉽게 list로 만들어 놓는 작업
    for i in range(1, len(s)-1 ) :
        if s[i] == "{" :
            index = i+1
        elif s[i] == "}" :
            buf = s[index : i]
            num_list.append(list(map(int, buf.split(","))))
            buf = ""
    
    #  dict 형식으로 만들어 해당하는 숫자가 어느 위치에 있는지 확인
    ans_dict = dict()
    for i in num_list :
        for j in i :
            if j in ans_dict :
                if ans_dict[j] > len(i) :
                    ans_dict[j] = len(i)
            else :
                ans_dict[j] = len(i)
    
    #  ditc 를 value 값을 기준으로 정렬하여 정답에 적재하는 작업
    buf = sorted(ans_dict.items(), key= lambda x: x[1])
    for i in buf :
        answer.append(i[0])
    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))