def solution(N, stages):
    stage_rate = dict()
    stages.sort()
    #print(stages)
    stage_passer = 0
    last_stage = 0
    analysis = len(stages)
    set_stages = list(set(stages))

    k = 1

    for i in range(N): 
        try : 
            analysis -= stage_passer
            stage_passer = stages.index(set_stages[k]) - stages.index(set_stages[k-1])
            last_stage += stage_passer
            k+=1
        except :
            if (i+1)== set_stages[k-1] :
                stage_passer = stages.count(set_stages[k-1])
                stage_rate[i+1] = stage_passer/(analysis)
                continue
            stage_rate[i+1] = 0
            continue


        #print('stage_passer ', stage_passer)
        #print('analysis ',analysis)
        stage_rate[i+1] = stage_passer/(analysis)

    answer = sorted(stage_rate, key=lambda k : stage_rate[k],reverse = True)

    print(stage_rate)
    print(answer)
    return answer