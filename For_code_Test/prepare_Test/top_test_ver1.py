def solution(heights):
    answer = []
    N = len(heights)
    for i in range(N) :
        buf = heights.pop()
        cnt = -1
        T = len(heights)
        for k in range(T, 0, -1) :
            if heights[k-1] > buf :
                answer.append(k)
                cnt = 1
                break
        if cnt == -1 :
            answer.append(0)
    
    answer.reverse()
    return answer


h = [5,4,3,2,1]	
print(solution(h))