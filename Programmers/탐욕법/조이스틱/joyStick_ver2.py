def solution(name):
    ansList = []
    answer = 0
    a_len = 0

    if "A" in name :
        A_Index = name.index("A")
        for a in name[A_Index :] :
            if a == "A" :
                a_len += 1
            else :
                break
        if a_len == len(name) : return 0


    else :
        A_Index = -1

    for i in name :
        answer += min(abs(ord("A")- ord(i)), abs(ord("Z") - ord(i) + 1))
    answer += len(name) - 1
    ansList.append(answer)
    if A_Index > -1 :
        answer = 0
        for i in name[: A_Index] :
            answer += min(abs(ord("A")- ord(i)), abs(ord("Z") - ord(i) + 1))
        answer += A_Index -1

        for i in range(len(name)-1,A_Index + a_len -1, -1) :
            answer += min(abs(ord("A")- ord(name[i])), abs(ord("Z") - ord(name[i]) + 1)) + 1
        ansList.append(answer)
    return min(ansList)

print(solution("BBAABBBAAAAAA"))