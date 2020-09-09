import copy
def solution(tickets):
    ticketsDict = dict()
    for i in tickets :
        temp = ''.join(i)
        if temp in ticketsDict :
            ticketsDict[temp] += 1
        else :
            ticketsDict[temp] = 1

    answer = []
    start_root = []
    for i in tickets :
        if i[0] == "ICN" :
            start_root.append(i)
    
    for i in start_root :
        ans_buf = [i[0], i[1]]
        checkTicket = copy.deepcopy(ticketsDict)
        cnt = 2
        while cnt < len(tickets) :
            for j in tickets :
                if j[0] == ans_buf[-1] :
                    temp = ''.join(j)
                    if checkTicket[temp] > 0 :
                        checkTicket[temp] -= 1
                        ans_buf.append(j[1])
            if len(ans_buf) == len(tickets) + 1 :
                answer.append(ans_buf)
            cnt += 1
    answer.sort()
    return answer[0]



print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
print(solution( [['ICN','A'],['ICN','A'],['A','ICN']]))