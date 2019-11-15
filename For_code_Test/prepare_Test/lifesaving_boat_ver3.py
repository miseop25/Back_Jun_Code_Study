def solution(people, limit):
    answer = 1
    people.sort()
    buf = people.pop()
    i = 0
    while len(people)-i>1 :
        if (limit - buf) >=40 :
            if (people[i]+ buf) <= limit :
                buf = people[i]+buf
                i +=1                        
            else :
                answer += 1
                buf = people.pop()
        else :
            answer +=1
            buf = people.pop()
    return answer

print(solution([70, 50, 80, 50],100))