def solution(n, arr1, arr2):
    answer = []
    ans_bin = []
    for i in range(n) :
        x = (arr1[i])
        y = (arr2[i])
        ans_bin.append(bin(x | y))
    for s in ans_bin :
        temp = s[2:]
        buf = ""
        if len(temp) != n :
            cnt = n - len(temp)
            temp = "0"*cnt + temp
        
        for strings in  temp :
            if strings == "0" :
                buf += " "
            else :
                buf += "#"
        answer.append(buf)

    return answer


print(solution(5,[9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))