def solution(msg):
    answer = []
    lzw_dict = dict()
    word = "A"
    for i in range(1, 27) :
        lzw_dict[word] = i
        word = chr(ord("A") + i )
    
    m_index = 0 
    w = msg[0]
    while m_index < len(msg):
        if m_index + 1 < len(msg) :
            temp = w + msg[m_index + 1]
        else :
            temp = w
            if temp in lzw_dict :
                answer.append(lzw_dict[temp])
            else :
                answer.append(lzw_dict[temp[: -1]])
            break
        if temp in lzw_dict :
            w = temp
            m_index += 1
        else :
            i+= 1
            lzw_dict[temp] = i
            answer.append(lzw_dict[temp[: -1]])
            m_index += 1
            w = msg[m_index]
        



    return answer

print(solution("KAKAO"))