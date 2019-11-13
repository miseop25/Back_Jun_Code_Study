def solution(skill, skill_trees):
    answer = 0
    sk_list = [*map(str,skill)]
    print(sk_list)
    for i in skill_trees :
        comp = 0
        cnt = 1
        for j in range(len(i)) :
            if i[j] in sk_list :
                if skill[comp] == i[j] :
                    cnt = 1
                    comp +=1
                else :
                    cnt = -1
                    break

        if cnt == 1:
            answer +=1
            
                
    return answer

sk = 'CBD'
skt = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(sk,skt))