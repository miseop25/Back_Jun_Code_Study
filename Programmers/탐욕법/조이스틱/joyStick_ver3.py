def solution(name):
    ansList = []
    answer = 0
    a_len = 0
    
    def findA() :
        A_Index = 0
        a_len = 0
        temp =[]
        while A_Index > -1 :
            if "A" in name[A_Index :] :
                A_Index = name.find("A", A_Index + a_len)
                if A_Index < 0 : break
                a_len = 0
                for a in name[A_Index :] :
                    if a == "A" :
                        a_len += 1
                    else :
                        break
                temp.append([A_Index, a_len])
            else :
                return temp
        return temp
    aList = findA()
    if aList :
        aList = sorted(aList, key= lambda x: -x[1])
        A_Index = aList[0][0]
        a_len = aList[0][1]
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