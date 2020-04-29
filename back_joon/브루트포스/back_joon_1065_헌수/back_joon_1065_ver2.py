def soluction(n) :
    if n <= 99 :
        return n
    elif n == 1000 :
        return 144
    else :
        answer = 99
        for i in range(100, n+1) :
            a1 = i//100
            a2 = i%100//10
            a3 = i%100%10
            if (a1 - a2) == ( a2 - a3) :
                answer += 1
    return answer


N = int(input())
print(soluction(N))
