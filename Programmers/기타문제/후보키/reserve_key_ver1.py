def solution(relation):
    answer = 0

    #  하나의 키 만으로 분류 가능한지?
    pass_list = []
    for i in range(len(relation[0])) :
        check_dict = dict()
        ck = True
        for j in range(len(relation)) :
            if relation[j][i]in check_dict :
                ck = False
                break
            else :
                check_dict[relation[j][i]] = 1
        if ck :
            answer += 1
            pass_list.append(i)
    
    print(pass_list)
    return answer




print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))