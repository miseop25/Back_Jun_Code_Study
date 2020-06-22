def solution(s):
    i = 1
    if len(s)%2 != 0 :
        return 0
    while i < len(s) :
        if s[i] == s[i-1] : 
            s = s[: i-1] + s[i + 1 : ]
            if i != 1 :
                i -= 1
        else :
            i += 1

    if len(s) == 0 :
        return 1
    else :
        return 0

print(solution("baabaa"))