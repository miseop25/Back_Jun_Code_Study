def solution(budgets, M) :
    budgets = sorted(budgets)
    st = 0
    ed = budgets[-1]

    while st <= ed :
        mid = (st+ed)//2
        n = 0
        for i in budgets :
            if i >= mid :
                n += mid
            else :
                n += i
        if n <= M :
            st = mid + 1
        else :
            ed = mid -1
    return ed
            
    
        


if __name__ == "__main__":
    N = int(input())
    budgets = list(map(int, input().split(" ")))
    M = int(input())
    print(solution(budgets, M))