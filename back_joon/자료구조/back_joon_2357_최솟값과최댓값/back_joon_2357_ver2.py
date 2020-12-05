import sys
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
        temp = sorted(self.num[a-1: b])
        return temp[0], temp[-1]
    
    def getAnswer(self) :
        for _ in range(self.M) :
            a, b = map(int, input().split(" "))
            minV, maxV = self.getMaxMin(a,b)
            print(minV, maxV)


if __name__ == "__main__":
    N, M = map(int, input().split(" "))
    t = Soluction(N, M) 
    t.getAnswer()