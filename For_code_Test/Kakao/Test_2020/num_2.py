def solution(s):
    answer = []
    buf = []
    cnt = 0
    for i in s :
        if i == '{' :
            buf.append([])
        elif i == '}' :
            cnt += 1
        try :
            num = int(i)
            buf[cnt].append(num)
        except :
            pass
    print(buf)
    return answer