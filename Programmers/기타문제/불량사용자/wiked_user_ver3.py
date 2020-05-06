import itertools

def solution(user_id, banned_id):
    ban = dict()
    cnt = 0
    for b in banned_id :
        real_str = b
        cnt +=  1
        # 중복되는 값을 방지하기 위해 뒤에 숫자를 붙인다.(중복되는 경우)
        if b in ban :
            b += str(cnt)
        ban[b] = []

        # 별의 우치를 찾는 작업
        star = []
        for s in range(len(real_str)) :
            if real_str[s] == "*" : 
                star.append(s)
        
        for u in user_id :
            temp = 0
            buf = ""
            #  제재 아이디의 별의 위치에 맞도록 user id 를 수정 -> 비교 진행
            for i in star :
                if len(u) > i : 
                    buf += u[temp : i] + "*"
                    temp = i + 1
            if len(u) != len(buf) :
                buf += u[temp :]
            if real_str == buf :
                ban[b].append(u)
    
    ban_list = list(ban.values())
    ans_list = list(itertools.product(*ban_list))
    answer = set()
    for a in ans_list:
        if len(set(a)) == len(banned_id):
            answer.add("".join(sorted(set(a))))

    return len(answer)


print(solution(
["frodo", "fradi", "crodo", "abc123", "frodoc"], 
["fr*d*", "abc1**"]))