def check(six) :
    strSix = str(six)
    cnt = -3
    for i in range(len(strSix)-1, -1, -1) :
        if strSix[i] == '6' :
            cnt += 1 
        else :
            break
    if cnt > 0 :        
        return 10**(cnt)
    else :
        return 1

    
def soluction(num) :
    answer = 1666
    count = 1
    i = 1
    if num == 1 :
        return 666
    while count < num :
        if str(i)[-1] == '6' :
            count += check(answer)
        else :
            count += 1
        i += 1
        if count > num :
            for _ in range(count - num - 1) :
                answer += 1
                return answer
        elif count == num :
            break
        answer += 1000
    return answer
    

N = int(input())
print(soluction(N))
