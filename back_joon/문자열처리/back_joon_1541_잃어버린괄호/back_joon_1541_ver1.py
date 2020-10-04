if __name__ == "__main__":
    word = input().rstrip()

    flag = True
    num = '0'
    answer = 0
    temp = 0
    minus = 0
    for i in word :
        if i != "+" and i != "-" :
            num += i
            continue
        if i == "+" :
            temp += int(num)
   
        else :
            temp += int(num)
            if flag :
                answer += temp
                temp = 0
                flag = False
            else :
                answer -= temp
                temp = 0

        num = '0'
    temp += int(num)
    if flag :
        answer += temp
    else :
        answer -= temp
    print(answer)


