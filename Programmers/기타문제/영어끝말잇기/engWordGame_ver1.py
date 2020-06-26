def solution(n, words):
    answer = []
    person = dict()
    di = dict()
    for i in range(1, n+1) :
        person[i] = 1
    endWord = words[0][-1]
    person[1] += 1
    di[words[0]] = True
    i = 2
    for w in words[1:] :
        if w in di or w[0] != endWord :
            answer.append(i)
            answer.append(person[i])
            return answer
        di[w] = True
        endWord = w[-1]
        person[i] += 1
        if i == n :
            i = 1
        else :
            i += 1

    return [0,0]

print(solution(2,['qwe', 'eqwe', 'eqwe']))