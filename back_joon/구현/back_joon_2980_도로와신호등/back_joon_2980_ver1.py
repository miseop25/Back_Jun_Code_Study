import sys
input = sys.stdin.readline

class Soluction :
    def __init__(self) :
        self.N = 0
        self.M = 0

        self.time = 0
        self.dis = 0

        self.signArray = []
    
    def firstInput(self) :
        self.N, self.M = map(int, input().split(' '))
        for _ in range(self.N) :
            self.signArray.append(list(map(int, input().split(" "))))

    def checkRed(self, R,G) :
        temp = self.time % (R+G)
        if temp < R :
            return R - temp
        else :
            return 0 
    
    def getAnswer(self) :
        for loca, R, G in self.signArray :
            self.time += (loca - self.dis)
            self.dis = loca
            self.time += self.checkRed(R,G)
        self.time += self.M - self.dis
        return self.time


if __name__ == "__main__":
    s = Soluction()
    s.firstInput()
    print(s.getAnswer())

    
