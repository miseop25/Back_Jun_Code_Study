def solution(n):
    answer = 0

    buf = [0,1]
    if n == 1 :
        return 1
    elif n == 2:
        return 2
    for i in range(n-1) :
        answer = buf.pop(0) + buf[0]
        buf.append(answer)

    
    return answer%1234567

print(solution(5))