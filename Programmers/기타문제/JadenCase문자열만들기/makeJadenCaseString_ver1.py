def solution(s):
    answer = []
    tmep = list(map(str, s.split(" ")))
    for i in tmep :
        if i == '' :
            answer.append(i)
            continue
        i = i.lower()
        if i[0] >= "0" and i[0] <= "9" :
            answer.append(i)
        else :
            buf = ''
            a = i[0].upper()
            buf = a + i[1: ]
            answer.append(buf)

    return ' '.join(answer)

print(solution("asdwqe  asdqw"))