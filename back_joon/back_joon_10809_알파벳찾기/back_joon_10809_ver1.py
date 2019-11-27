def find_abc(S) :
    answer = ''
    buf_list = list()
    for _ in range(26) :
        buf_list.append(-1)
    
    for i in range(len(S)) :
        buf = ord(S[i]) - 97
        if buf_list[buf] == -1 :
            buf_list[buf] = i

    answer = str(buf_list[0])
    for i in buf_list[1 :] :
        answer += ' '
        answer += str(i)

    return answer


S = input()
print(find_abc(S))