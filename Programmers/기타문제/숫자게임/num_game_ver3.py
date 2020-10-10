from collections import deque
def solution(A, B):
    answer = 0
    b = deque(sorted(B, key= lambda x: -x))
    a = deque(sorted(A, key= lambda x: -x))
    while a :
        if a[0] < b[0] :
            a.popleft()
            b.popleft()
            answer += 1
        else :
            a.popleft()
    return answer

print(solution([5, 1, 3, 7], [2, 2, 6, 8]))