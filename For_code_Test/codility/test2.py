# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    str_len = len(S)//2
    re_ha_S = S[str_len :]
    re_ha_S = re_ha_S[::-1]

    if len(S)%2 == 1 :
        ha_S = S[:str_len+1]
        str_len +=1
    else :
        ha_S = S[:str_len]


    first = str()
    second = str()

    for i in range(str_len) :
        if ha_S[i] != re_ha_S[i] and ha_S[i] != '?' and re_ha_S[i] != '?' :
            return 'NO'
        elif ha_S[i] != re_ha_S[i] and ha_S[i] == '?' :
            first += re_ha_S[i]
            second  += re_ha_S[i]
        elif ha_S[i] != re_ha_S[i] and re_ha_S[i] == '?' :
            first += ha_S[i]
            second  += ha_S[i]
        elif ha_S[i] == re_ha_S[i] and ha_S[i] == '?' and re_ha_S[i] == '?' :
            first += 'a'
            second  += 'a'
        elif ha_S[i] == re_ha_S[i] :
            first += ha_S[i]
            second += re_ha_S[i]
    
    if len(S)%2 == 1 :
        second = second[0: :-1]
    else :
        second = second[::-1]

    return (first + second)


print(solution("?ab??a"))
print(solution("bab??a"))
print(solution("?a?"))