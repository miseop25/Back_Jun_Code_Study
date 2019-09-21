def solution(progresses, speeds):
    answer = []
    comps_list = []
    speed_comp_list =[]
    completed = 0
    day = 1

    while day < 100 :
        if len(progresses) == 0 :
            day = 200
            break

        for i in range(len(progresses)) :
            progresses[i] += speeds[i] 

        if progresses[0] >=100 :
            print(len(comps_list))
            print(speed_comp_list)
            for i in range(len(progresses)) :
                if progresses[i] >= 100 :
                    completed +=1
                    comps_list.append(progresses[i])
                    speed_comp_list.append(speeds[i])
            for k in range(len(comps_list)) :
                progresses.remove(comps_list[k])
                speeds.remove(speed_comp_list[k])


            answer.append(completed)
            comps_list.clear()
            speed_comp_list.clear()
            completed = 0
        day +=1
    return answer


pro = [93,30,55]
spe = [1,30,5]

print(solution(pro,spe))