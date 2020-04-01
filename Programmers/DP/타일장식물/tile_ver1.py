def solution(N):
    answer = 0
    mem = [4,6]
    if N == 1 :
        answer = 4
    elif N == 2 :
        answer = 6
    else :
        for _ in range(N-2) :
            answer = mem.pop(0) + mem[0]
            mem.append(answer)



    return answer