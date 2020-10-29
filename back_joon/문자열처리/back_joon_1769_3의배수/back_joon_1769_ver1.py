if __name__ == "__main__":
    N = (input())
    cnt = 0
    while int(N) > 9  :
        temp = 0
        for i in N :
            temp += int(i)
        N = str(temp)
        cnt += 1
    
    if int(N)%3 == 0 :
        answer = "YES"
    else :
        answer = "NO"
    print(cnt)
    print(answer)