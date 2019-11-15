def solution(people, limit):
    answer = 1
    people.sort()
    buf = people.pop()
    cnt = 1
    while people :
        if (limit - buf) >=40 :
            if (people[0]+ buf) <= limit :
                buf = people[0]+buf                        
                people.pop(0)
            else :
                answer += 1
                buf = people.pop()
        else :
            answer +=1
            buf = people.pop()
    return answer

print(solution([70, 50, 80, 50],100))