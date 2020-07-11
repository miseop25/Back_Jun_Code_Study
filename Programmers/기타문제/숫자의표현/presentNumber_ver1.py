def solution(n):
    answer = 1
    st = n//2 + 1
    while True :
        check = 0
        flag = True
        for i in range(st, 0, -1) :
            check += i
            if check == n :
                answer += 1
                flag = False
                break
            elif check > n :
                break
        if flag :
            if check == n :
                answer += 1
            elif check < n :
                return answer
        st -= 1
    return answer