def checkSong(keyword, array) :
    cnt = 0
    front = True 
    index = keyword.find("?")
    if index == 0 :
        for i in range(len(keyword)) :
            if keyword[i] != "?" :
                index = i 
                break
    else : 
        front = False
    lentgh = len(keyword)
    for a in array :
        if lentgh == len(a) :
            if front :
                if keyword[index : ] == a[index: ] :
                    cnt += 1
            else :
                if keyword[: index] == a[:index] :
                    cnt += 1
    return cnt


def solution(words, queries):
    answer = []
    for i in queries :
        answer.append(checkSong(i, words))
    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["fro??", "????o", "fr???", "fro???", "pro?"] ))