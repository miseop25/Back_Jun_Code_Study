
def solution(budgets, M):
    answer = 0
    budgets = sorted(budgets)
    price = 0
    for i in budgets :
        if price + i <= M :
            price += i
            answer += 1

        
    return answer


print(solution([1,3,2,5,5], 9))