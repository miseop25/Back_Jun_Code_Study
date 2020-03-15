def solution(participant, completion):

    s1 = set(participant)
    s2 = set(completion)
    answer = list(s1 -s2)
    if answer :
        return answer[0]
    participant.sort()
    completion.sort()
    for i in range(len(participant)) :
        if participant[i] != completion[i] :
            return participant[i]