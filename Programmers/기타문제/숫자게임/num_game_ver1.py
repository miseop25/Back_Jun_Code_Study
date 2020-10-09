from collections import deque
def solution(A, B):
    answer = 0
    result = []
    b = deque(B)
    a = deque(A)
    while a :
        comp = a.popleft()
        temp = deque(sorted(b, key=lambda x: abs(comp+1-x)   ))
        result.append(temp.popleft())
        b = list(temp)

    for i in range(len(A)) :
        if A[i] < result[i] :
            answer += 1

    return answer