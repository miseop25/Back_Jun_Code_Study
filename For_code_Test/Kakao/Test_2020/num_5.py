def solution(stones, k):
    answer = 0

    while True :
        cnt = 1
        for i in range(len(stones)):
            if stones[i] != 0 :
                stones[i] -=1
                cnt = 1
            else :
                cnt += 1
            if cnt > k :
                break
        if cnt > k :
            break
        else :
            answer +=1
    return answer