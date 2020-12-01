import sys
import heapq

input = sys.stdin.readline

if __name__ == "__main__":
    T = int(input())
    num = []
    for i in range(T) :
        temp = input().rstrip()
        heapq.heappush(num, (float(temp), temp )  )
        if i > 8 :
            heapq.heappop(num)
    for i in range(7) :
        result = heapq.heappop(num)
        print('%0.3f' % result[0])
