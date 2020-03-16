import collections
import heapq

def solution(stock, dates, supplies, k):
    answer = 0
    factory = dict(zip(dates, supplies))
    day = 0
    i = 0
    while stock <= k :
        stock -= 1
        day += 1
        k -= 1
        if day == dates[i] :
            if (stock + supplies[i]) >= k :
                stock = stock + supplies[i]
                answer += 1 
            
            elif i < (len(dates)-1) :
                if stock < (dates[i+1] - day) :
                    stock = stock + supplies[i]
                    answer += 1

            if i < len(dates)-1:
                i += 1
    
    print(factory)

    return answer

print(solution(4,[4,10,15],[20,5,10],30))


