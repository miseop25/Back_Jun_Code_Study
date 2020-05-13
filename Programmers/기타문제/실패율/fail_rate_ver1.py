def solution(N, stages):
    answer = []
    st_dict = dict()
    ans_dict = dict()
    for i in range(1, N + 1) :
        st_dict[i] = [0,0]
        ans_dict[i] = 0
        #  [0] = 스테이지에 도달한 사람 [1] = 도달했으나 클리어하지 못한 사람
    for s in stages :
        for i in range(1, s ) :
            st_dict[i][0] += 1
        if s <= N :
            st_dict[s][1] += 1
            st_dict[s][0] += 1
    
    #  실패율을 계산!! 
    for k, v in st_dict.items() :
        if v[0] == 0 :
            ans_dict[k] = 0
        else :
            ans_dict[k] = v[1]/v[0]
    
    result = list(sorted(ans_dict.items(), key= lambda x: (-x[1], x[0] )))
    for i in result :
        answer.append(i[0])

    return answer

# print(solution(5, [4, 4, 4, 4, 4]))
print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]   ))
print(solution(2, [2,1]   ))
