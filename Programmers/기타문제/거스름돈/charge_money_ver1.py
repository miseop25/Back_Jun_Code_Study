def solution(n, money):
    answer = 0
    money.sort()
    print(money)
    for i in range(len(money)) :
        val, leav = divmod(n, money[i])
        if leav == 0 :
            answer += 1
        while val > 0 :
            charge = n - val*money[i]
            if charge == 0 :
                val -= 1
                continue
            for j in range(len(money[:i])) :
                val_2, leav_2 = divmod(charge, money[j])
                if leav_2 == 0 :
                    answer += 1
            val -= 1
    return answer%1000000007

print(solution(10,[1,2,5]))