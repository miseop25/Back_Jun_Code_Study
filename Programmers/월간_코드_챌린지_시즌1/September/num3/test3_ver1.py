def solution(a):
    if len(a) < 3 :
        return len(a)
    answer = 2

    x = min(a[:1])
    y = min(a[2:])

    for i in range(1, len(a)-1) :
        if a[i] < x or a[i] < y :
            if a[i] < x :
                x = a[i]
            answer +=1

        if a[i+1] == y  and i+2 < len(a):
            y = min(a[i+2:])

    return answer

print(solution([9,-1,-5]))
print(solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]))