def soluction(n, cnt) :
    finger = [[8], [6,2], [4], [2,6], [8]]
    answer = 0
    if cnt == 1 :
        answer += n + finger[n-1][0] - 1
        return answer
    
    if n == 1 or n == 3 or n == 5 :
        answer += n + (cnt)*sum(finger[n-1]) - 1
        return answer
    elif n == 2 :
        v, r= divmod(cnt+1, 2)
        answer = v*8 - 1
        if r != 0 :
            if cnt%2 == 0 :
                answer += finger[n-1][1]
            else :
                answer += finger[n-1][0]    
    else :
        v, r= divmod(cnt, 2)
        answer += n + v*8 - 1
        if r != 0 :
            if cnt%2 == 0 :
                answer += finger[n-1][1]
            else :
                answer += finger[n-1][0]   
    return answer


if __name__ == "__main__":
    n = int(input())
    cnt = int(input())
    print(soluction(n,cnt))