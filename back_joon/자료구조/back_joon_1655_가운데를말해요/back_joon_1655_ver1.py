import heapq
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    maxHeap = []
    minHeap = []
    N = int(input())
    firstNum = int(input())
    heapq.heappush(maxHeap, (-firstNum, firstNum))
    print(maxHeap[0][1])

    for _ in range(N-1) :
        num = int(input())
        if num > maxHeap[0][1] :
            heapq.heappush(minHeap, num)
        else : 
            heapq.heappush(maxHeap, (-num, num))
        
        if len(maxHeap) > len(minHeap) + 2 :
            temp = heapq.heappop(maxHeap)
            heapq.heappush(minHeap, temp[1])
        elif len(maxHeap) < len(minHeap) :
            temp = heapq.heappop(minHeap) 
            heapq.heappush(maxHeap, (-temp, temp))
        print(maxHeap[0][1])