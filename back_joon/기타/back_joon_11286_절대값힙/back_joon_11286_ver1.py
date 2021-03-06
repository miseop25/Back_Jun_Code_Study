import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = []
heapq.heapify(heap)
for _ in range(N) :
    temp = int(input())
    if temp != 0 :
        heapq.heappush(heap, (abs(temp), temp))
    else :
        if heap :
            print(heapq.heappop(heap)[1])
        else :
            print(0)
