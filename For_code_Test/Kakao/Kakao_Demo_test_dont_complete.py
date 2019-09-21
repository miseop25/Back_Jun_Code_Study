def solution(participant, completion):


    s1 = set(participant)
    s2 = set(completion)
    answer = list(s1 -s2)
    if answer :
        return answer[0]
    
    overlab_list = []
    for i in participant :
        if participant.count(i) >1 :
            overlab_list.append(i)
    
    s3 = list(set(overlab_list))
    for i in s3 :
        if overlab_list.count(i) != completion.count(i) :
            return i

    for i in completion :
        participant.remove(i)
    print(participant)

    return participant[0]


