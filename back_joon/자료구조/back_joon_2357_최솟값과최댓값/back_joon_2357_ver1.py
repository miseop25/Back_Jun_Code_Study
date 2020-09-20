import sys
import heapq
input = sys.stdin.readline

class Soluction :
    def __init__(self, N,M) :
        self.M = M

        self.num = []
        self.inputNum(N)

    def inputNum(self, N) :
        for _ in  range(N) :
            self.num.append(int(input()))
    
    def getMaxMin(self, a, b) :
        maxHeap = []
        minHeap = []

        for i in self.num[a-1 :b] :
            heapq.heappush(maxHeap, (-i, i) )
            heapq.heappush(minHeap, i)
        return minHeap[0], maxHeap[0][1]
    
    def getAnswer(self) :
        for _ in range(self.M) :
            a, b = map(int, input().split(" "))
            minV, maxV = self.getMaxMin(a,b)
            print(minV, maxV)


if __name__ == "__main__":

    N, M = map(int, input().split(" "))
    t = Soluction(N, M) 
    t.getAnswer()