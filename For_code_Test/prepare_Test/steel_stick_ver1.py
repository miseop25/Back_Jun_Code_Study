def solution(arrangement):
    answer = 0
    stack = []
    i = 0
    N = len(arrangement)
    while i < N :
        if arrangement[i:i+2] == '()' :
            if stack :
                #stack = list(map(lambda x : x+1 , stack))
                answer += len(stack)
                i = i+2
            else :
                i = i+2
        elif arrangement[i] =='(' :
            stack.append(1)
            i +=1
        elif arrangement[i] == ')':
            answer += stack.pop()
            i+=1
    return answer

t = '()(((()())(())()))(())'
print(solution(t))