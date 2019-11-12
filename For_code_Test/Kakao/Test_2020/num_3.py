def comp_id(user, ban) :
    ans = 0
    if len(user) != len(ban) :
        return ans
    for i in range(len(ban)) :
        try :
            if ban[i] == user[i] :
                ans = 1
            elif ban[i] == '*':
                ans = 1
            else :
                ans = 0
                break
        except :
            pass
    return ans



def solution(user_id, banned_id):
    answer = 0
    answer_buf = []
    k= 0
    count = 0
    buf_id = user_id
    while True :
        ans = 0
        cnt = 0
        if count == 0 :
            buf_id = user_id
        else : 
            count = 0
        buf_list = []
        for b in range(len(banned_id)) :
            if count == 1 :
                break
            for ids in buf_id :
                ans = comp_id(ids,banned_id[b])
                if count == 1:
                    break
                if ans == 1 :
                    if k == 0 :
                        buf_list.append(ids)
                        cnt = cnt +1
                        break
                    else : 
                        for i in range(len(answer_buf)) :
                            if ids == answer_buf[i][b] :
                                buf_id.remove(ids)
                                count = 1
                        if count != 1 :
                            buf_list.append(ids)
                            cnt = cnt +1
                            break
        k = k+1
        if count != 1:
            if cnt == len(banned_id) :
                answer_buf.append(buf_list)
                answer = answer +1
                count = 0
            elif cnt == 0 :
                break
    return answer


id= ["frodo", "fradi", "crodo", "abc123", "frodoc"]
be = ["fr*d*", "abc1**"]
print(solution(id, be))