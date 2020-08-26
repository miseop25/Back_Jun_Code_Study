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
    wordDict = dict()
    for i in words :
        length = len(i)
        if length in wordDict :
            wordDict[length].append(i)
        else :
            wordDict[length] = [i]

    for i in queries :
        if len(i) in wordDict :
            answer.append(checkSong(i, wordDict[len(i)]))
        else :
            answer.append(0)
    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["fro??", "????o", "fr???", "fro???", "pro?"] ))