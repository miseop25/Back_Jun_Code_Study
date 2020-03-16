import heapq

def solution(stock, dates, supplies, k):
    answer = 0
    i_index = 0
    que = []
    while stock < k :
        for i in range(i_index, len(dates)) :
            if stock < dates[i] :
                break
            heapq.heappush(que, -supplies[i])
            i_index = i+1
        stock += (heapq.heappop(que) * -1)
        answer += 1
    
    
    return answer

print(solution(4,[4,10,15],[20,5,10],30))


