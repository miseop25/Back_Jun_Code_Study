import sys
input = sys.stdin.readline

class Soluction :
    def __init__(self, n):
        self.n = n
        self.cnt = 1
        self.arr = []
        self.end = 0
        self.max = [0,0]

    def getArr(self) :
        for i in range(self.n) :
            num = int(input().rstrip())
            self.arr.append(num)
            if self.max[0] <= num :
                self.max[0] = num
                self.max[1] = i


    def checkCount(self) :
        self.end = self.arr[-1]
        for i in range(self.n - 2, self.max[1]-1, -1 ) : 
            if self.arr[i] > self.end :
                self.cnt += 1
                self.end = self.arr[i]
    
    def getAnswer(self) : 
        self.getArr()
        self.checkCount()
        return self.cnt

if __name__ == "__main__" :
    n = int(input().rstrip())
    s = Soluction(n)
    print(s.getAnswer())