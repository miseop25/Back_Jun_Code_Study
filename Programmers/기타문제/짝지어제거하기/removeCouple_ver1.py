def solution(s):
    cnt = 0
    if len(s)%2 != 0 :
        return 0
    while cnt > -1 :
        temp = ""
        i = 0
        while i < len(s)-1 :
            if s[i] == s[i+1] :
                i += 2
                cnt += 1
            else :
                temp += s[i]
                i += 1
        if cnt > 0 :
            s = temp
            cnt = 0
        else :
            cnt = -1
    

    if len(s) == 0 :
        return 1
    else :
        return 0

print(solution("baabaa"))