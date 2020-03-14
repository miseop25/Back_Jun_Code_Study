import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    while scoville :
        try :
            if int(scoville[0]) >= int(K) :
                return cnt
            heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville)*2)
            cnt+=1
        except :
            return -1