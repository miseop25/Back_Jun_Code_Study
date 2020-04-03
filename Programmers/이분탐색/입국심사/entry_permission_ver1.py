def solution(n, time):
    left = 1
    right = max(time)*n
    answer = 0
    while left <= right :
        mid = (left + right)//2
        people = 0
        for i in time :
            people += mid//i
            if people >= n :
                break

        if people >= n :
            answer = mid
            right = mid -1
        else :
            left = mid + 1

    return answer



print(solution(6, [7,10]))