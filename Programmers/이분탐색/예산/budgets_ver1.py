import collections
def solution(budgets, M):
    answer = 0
    if sum(budgets) <= M :
        return max(budgets)
    val , num = divmod(M, len(budgets))
    budgets = sorted(budgets)
    que = collections.deque(budgets)
    price = M
    while que :
        if que[0] <= val :
            price -= que.popleft()
        elif val*len(que) < price :
            val += 1
        else : 
            answer = val - 1
            break
        
    return answer


print(solution([120, 110, 140, 150], 485))