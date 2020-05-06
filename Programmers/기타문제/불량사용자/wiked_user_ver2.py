import itertools

def solution(user_id, banned_id):
    ban = dict()
    cnt = 0
    for b in banned_id :
        real_str = b
        cnt +=  1
        if b in ban :
            b += str(cnt)
        ban[b] = []
        # find star
        star = []
        for s in range(len(real_str)) :
            if real_str[s] == "*" : 
                star.append(s)
        
        for u in user_id :
            temp = 0
            buf = ""
            for i in star :
                if len(u) > i : 
                    buf += u[temp : i] + "*"
                    temp = i + 1
            if len(u) != len(buf) :
                buf += u[temp :]

            if real_str == buf :
                ban[b].append(u)
    ban_list = list(ban.values())
    if len(banned_id) == 2 :
        ans_list = list(itertools.product(ban_list[0], ban_list[1] ))
    elif len(banned_id) == 3 :
        ans_list = list(itertools.product(ban_list[0], ban_list[1], ban_list[2] ))
    elif len(banned_id) == 4 :
        ans_list = list(itertools.product(ban_list[0], ban_list[1], ban_list[2], ban_list[3] ))
    elif len(banned_id) == 5 :
        ans_list = list(itertools.product(ban_list[0], ban_list[1], ban_list[2], ban_list[3], ban_list[4] ))
    elif len(banned_id) == 6 :
        ans_list = list(itertools.product(ban_list[0], ban_list[1], ban_list[2], ban_list[3], ban_list[4], ban_list[5] ))
    elif len(banned_id) == 7 :
        ans_list = list(itertools.product(ban_list[0], ban_list[1], ban_list[2] , ban_list[3], ban_list[4], ban_list[5], ban_list[6]))
    elif len(banned_id) == 8 :
        ans_list = list(itertools.product(ban_list[0], ban_list[1], ban_list[2], ban_list[3], ban_list[4], ban_list[5], ban_list[6], ban_list[7] ))
    else :
        return len(ban_list[0])
    new_ans_list = []
    for i in range(len(ans_list)) :
        cnt = len(ans_list[i])
        ch = list(set(ans_list[i]))
        if len(ch) == cnt :
            binary = 0b00000000
            for j in ch :
                a = user_id.index(j)
                binary = binary | (0b00000001 << a)
            if binary not in new_ans_list :
                new_ans_list.append(binary)

    return len(new_ans_list)


print(solution(
["frodo", "fradi", "crodo", "abc123", "frodoc"], 
["fr*d*", "abc1**"]))