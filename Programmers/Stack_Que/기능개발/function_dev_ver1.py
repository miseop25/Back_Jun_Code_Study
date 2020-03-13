def solution(progresses, speeds):
    answer = []
    completed = 0
    day = 1
    while day < 100 :
        if len(progresses) == 0 :
            day = 200
            break

        for i in range(len(progresses)) :
            progresses[i] += speeds[i] 
        
        while True :
            if progresses[0] > 99 :
                completed +=1
                progresses.pop(0)
                speeds.pop(0)

            else :
                break
            if len(progresses) == 0 :
                break
        if completed >0 :
            answer.append(completed)
            completed = 0
        
        day += 1


    return answer