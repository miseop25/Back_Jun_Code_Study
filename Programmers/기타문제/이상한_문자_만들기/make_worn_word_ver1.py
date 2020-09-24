def solution(s):
    answer = ''
    ansList = []
    words = list(s.split(" "))
    for w in words :
        temp = ''
        for i in range(len(w)) :
            if i %2 == 0 :
                temp += w[i].upper()
            else :
                temp += w[i].lower()
        ansList.append(temp)
    answer = ' '.join(ansList)
    return answer