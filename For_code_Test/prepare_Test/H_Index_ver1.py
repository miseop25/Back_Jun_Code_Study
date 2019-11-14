def solution(citations):
    answer = 0
    
    citations.sort(reverse=True)
    for i in range(len(citations)) :
        if  citations[i] > answer :
            answer +=1
        elif citations[i] < answer :
            if answer == (i) :
                return answer

    return answer

    

print(solution([3, 0, 6, 1, 5]))