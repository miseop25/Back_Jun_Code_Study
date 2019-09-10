def solution(N, stages):
    analysis = len(stages)

    stage_rate = dict()
    for i in range(N):
        k = stages.count(i+1)
        stage_rate[i+1] = k/analysis
        analysis -= k

    answer = sorted(stage_rate, key=lambda k : stage_rate[k],reverse = True)
    print(stage_rate)

    return answer