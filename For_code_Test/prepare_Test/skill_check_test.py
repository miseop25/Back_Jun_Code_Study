def solution(s):
    N = [l for l in s.split()]
    buf = ''
    answer = ''
    for i in range(len(N)) :
        N[i].capitalize()
        buf = ''
        for k in range(len(N[i])) :
            if int(k%2) ==0 :
                buf += N[i][k].upper()
            else :
                buf += N[i][k].lower()
        answer = answer +buf + ' '
    answer.rstrip()
    print(answer)
    
    return answer