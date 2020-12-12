import sys
input = sys.stdin.readline

class Soluction :
    def __init__(self, N,M) :
        self.N = N
        self.M = M

        self.webDict = dict()
    
    def inputWebPassword(self) :
        for _ in range(self.N) :
            web, password = input().rstrip().split(" ")
            self.webDict[web] = password
    
    def getAnswer(self) :
        for _ in range(self.M) :
            web = input().rstrip()
            print(self.webDict[web])

if __name__ == "__main__":
    N,M = map(int, input().split(" "))
    s = Soluction(N,M)
    s.inputWebPassword()
    s.getAnswer()