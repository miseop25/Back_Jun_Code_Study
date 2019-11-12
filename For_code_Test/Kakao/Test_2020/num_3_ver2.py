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
    answer = 1
    answer_buf = []
    for i in range(len(banned_id)) :
        answer_buf.append([])
        for k in user_id :
            ans = comp_id(k,banned_id[i])
            if ans == 1 :
                answer_buf[i].append(k)
    buf = []
    for i in answer_buf :
        answer = answer*len(i)
    return answer


id= ["frodo", "fradi", "crodo", "abc123", "frodoc"]
be = ["fr*d*", "*rodo", "******", "******"]	
print(solution(id, be))