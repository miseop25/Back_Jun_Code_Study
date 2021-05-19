class Soluction :
    def __init__(self, a,b):
        self.end = b
        self.st = a
        self.arr = []
    
    def makeArr(self) :
        num = 1
        cnt = 0
        while self.end >= cnt :
            for i in range(1, num + 1) :
                self.arr.append(num)
                cnt += 1
            num += 1

    
    def getAnswer(self) :
        self.makeArr()
        targetArr = self.arr[self.st-1 : self.end]
        return sum(targetArr)


if __name__ == "__main__" :
    a,b = map(int, input().split(" "))
    s = Soluction(a,b)
    print(s.getAnswer())
