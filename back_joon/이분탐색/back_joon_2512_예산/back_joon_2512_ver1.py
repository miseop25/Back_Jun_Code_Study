def solution(budgets, M) :
    budgets = sorted(budgets)
    st = 0
    ed = budgets[-1]
    mid = (sum(budgets)) // len(budgets)

    while ed-st > 1 :
        price = M
        for i, v in enumerate(budgets) :
            if v <= mid :
                price -= v
            else :
                break
        price -= (len(budgets)- i)*mid
        if price == 0 :
            return mid
        elif price < 0 :
            ed = mid
            mid = (st + mid)//2
            
        else :
            if ed - mid == 1:
                mid = ed 
            else :
                st = mid 
                mid = (ed + mid)//2

    return mid
            
    
        


if __name__ == "__main__":
    N = int(input())
    budgets = list(map(int, input().split(" ")))
    M = int(input())
    print(solution(budgets, M))