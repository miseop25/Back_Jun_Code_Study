def solution(people, limit):
    answer = 1
    people.sort()
    buf = people[0]
    for i in people[1 :] :
        if (limit-buf) >40 :
            if (buf+i) > limit :
                buf = i 
                answer+=1
        else :
            buf = i
            answer+=1
    print(people)

    return answer

print(solution([70, 50, 80, 50],100))