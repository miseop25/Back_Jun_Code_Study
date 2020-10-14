def solution(gems):
    answer = []

    setGems = set(gems)
    g_len = len(setGems)
    myGems = dict()
    m_len = 0

    i = 0
    j = 0
    flag = True

    while j < len(gems) or not flag :
        if flag :
            if gems[j] not in myGems :
                myGems[gems[j]] = 1
                m_len += 1
            else :
                myGems[gems[j]] += 1
            j += 1
        else :
            myGems[gems[i]] -= 1
            if myGems[gems[i]] == 0 :
                myGems.pop(gems[i])
                m_len -= 1
            i += 1

        if m_len == g_len :
            flag = False
            answer.append([i+1,j])
        else :
            flag = True


    result = sorted(answer, key= lambda x: ((x[1]-x[0]), x[0])   )

    return result[0]

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["a", "a", "b"]))