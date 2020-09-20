def solution(budgets, M) :
    budgets = sorted(budgets)
    left = 0
    right = budgets[-1]
    mid = (left + right)//2

    while left <= right :
        price = M 
        for i in budgets :
            if i <= mid :
                price -= i
            else :
                price -= mid
        
        if price < 0 :
            right = mid - 1
            mid = (left + right)//2
        else :
            left = mid + 1
            mid = (left + right)//2
    return right

    
        


if __name__ == "__main__":
    N = int(input())
    budgets = list(map(int, input().split(" ")))
    M = int(input())
    print(solution(budgets, M))