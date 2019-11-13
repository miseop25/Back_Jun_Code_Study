def solution(skill, skill_trees):
    answer = 0
    sk_list = [*map(str,skill)]
    print(sk_list)
    for i in skill_trees :
        for j in i :
            if j in sk_list :
                print(j)
    return answer

sk = 'CBD'
skt = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(sk,skt))