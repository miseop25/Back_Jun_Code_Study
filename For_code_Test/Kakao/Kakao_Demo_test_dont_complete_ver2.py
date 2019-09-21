def solution(participant, completion):


    #li_to_part = {i : participant.count(i) for i in participant}
    participant.sort()
    completion.sort()
    for i in range(len(participant)) :
        if participant[i] != completion[i] :
            return participant[i]
        else :
            return participant.pop()




