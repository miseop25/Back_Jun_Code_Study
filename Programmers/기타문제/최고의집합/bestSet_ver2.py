def solution(n, s):
    answer = []
    v, r = divmod(s, n)
    if v == 0 :
        return [-1]
    if r == 0 :
        return [v]*n
    
    for i in range(n) :
        if i < r :
            answer.append(v+1)
        else :
            answer.append(v)
    return sorted(answer)

print(solution(3,123))
print(solution(2,9))