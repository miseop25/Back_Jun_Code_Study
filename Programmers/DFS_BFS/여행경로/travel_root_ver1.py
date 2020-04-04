def solution(tickets):
    answer = []
    start_root = []
    for i in tickets :
        if i[0] == "ICN" :
            start_root.append(i)
    
    for i in start_root :
        ans_buf = [i[0], i[1]]
        stack = [i]
        while len(stack) != len(tickets) :
            for j in tickets :
                if j[0] == ans_buf[len(ans_buf)-1] :
                    if j not in stack :
                        stack.append(j)
                        ans_buf.append(j[1])
            if len(ans_buf) == len(tickets) + 1 :
                answer.append(ans_buf)
    
    answer.sort()
    return answer[0]

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))