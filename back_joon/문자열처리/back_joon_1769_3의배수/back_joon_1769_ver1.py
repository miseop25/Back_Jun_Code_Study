if __name__ == "__main__":
    N = int(input())
    total = len(str(N))
    cnt = 0
    while total >1  :
        temp = 0
        check = 1
        total = 0
        for i in str(N) :
            temp += int(i)
            if temp >= check :
                total += 1
                check *= 10
        N = temp
        cnt += 1
    
    if N%3 == 0 :
        answer = "YES"
    else :
        answer = "NO"
    print(cnt)
    print(answer)