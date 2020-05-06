import itertools

def solution(user_id, banned_id):
    answer = 0
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

    print(ban_list)

    return answer

