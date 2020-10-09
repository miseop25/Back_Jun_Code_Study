from collections import deque
def solution(A, B):
    answer = 0
    result = []
    b = deque(B)
    a = deque(A)
    while a :
        comp = a.popleft()
        temp = deque(sorted(b, key=lambda x: x-comp if comp < x else x*1000000000 ))
        if temp[0] > comp :
            answer += 1
            result.append(temp.popleft())
        else :
            result.append(temp.pop())
        b = list(temp)

    

    return answer

print(solution([5, 1, 3, 7], [2, 2, 6, 8]))