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
    #  곱집합을 재재 리스트에 있는 아이디 들로 곱집합을 구하는 과정
    #  -> 중복을 포함해서 모든 경우의 수를 구할 수 있다.
    ans_list = list(itertools.product(*ban_list))
    answer = set()
    for a in ans_list:
        # set 으로 중복을 제거했을때 항목 수가 줄어들었으면 pass 한다.
        if len(set(a)) == len(banned_id):
            #  정렬 후 문자열로 만들어 집어 넣어 중목을 방지한다.
            #  같은 것이 두개 들어가도 set로 설정되어 있기 때문에 중복되지 않는다.
            answer.add("".join(sorted(set(a))))

    return len(answer)


print(solution(
["frodo", "fradi", "crodo", "abc123", "frodoc"], 
["fr*d*", "abc1**"]))