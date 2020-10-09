from collections import deque
def solution(A, B):
    answer = 0
    result = []
    b = deque(B)
    a = deque(A)
    while a :
        comp = a.popleft()
        b = deque(sorted(b, key=lambda x: x if comp < x else (-x + 1000000000) ))
        if b[0] > comp :
            answer += 1
            result.append(b.popleft())
        else :
            result.append(b.pop())
       

    return answer

print(solution([5, 1, 3, 7], [2, 2, 6, 8]))