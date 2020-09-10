from collections import deque

def solution(a):
    if len(a) < 3 :
        return len(a)
    answer = 2

    x = min(a[:1])
    left = set(a[:1])
    right = deque(sorted(a[2:]))
    for i in range(1, len(a)-1) :
        if a[i] < x or a[i] < right[0] :
            if a[i] < x :
                x = a[i]
            answer +=1
        left.add(a[i+1])
        while right :
            if right[0] in left :
                right.popleft()
            else :
                break
    return answer

print(solution([9,-1,-5]))
print(solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]))