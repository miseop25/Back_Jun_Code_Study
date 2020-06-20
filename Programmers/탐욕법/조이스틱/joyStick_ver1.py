def solution(name):
    ansList = []
    answer = 0
    for i in name :
        answer += min(abs(ord("A")- ord(i)), abs(ord("Z") - ord(i) + 1))
    answer += len(name) - 1
    ansList.append(answer)
    answer = 0
        for i in range(0, -len(name), -1) :
            answer += min(abs(ord("A")- ord(name[i])), abs(ord("Z") - ord(name[i]) + 1))
    answer += len(name) - 1
    ansList.append(answer)
    return min(ansList)
print(solution("JEROEN"))