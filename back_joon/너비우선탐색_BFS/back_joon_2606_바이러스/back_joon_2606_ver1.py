import sys
input = sys.stdin.readline

class Soluction :
    def __init__(self, N) :
        self.nodeDict = dict()
        self.bfs = [False]*(N+1)
        self.bfs[0] = True
        self.bfs[1] = True
        self.answer = 0
        for i in range(1, N+1) :
            self.nodeDict[i] = []

    def inputNode(self, C) :
        for _ in range(C) :
            a, b = map(int, input().split(" "))
            self.nodeDict[a].append(b)
            self.nodeDict[b].append(a)
    
    def checkTree(self, st) :
        for i in self.nodeDict[st] :
            if not self.bfs[i] :
                self.answer += 1
                self.bfs[i] = True
                self.checkTree(i)

    def printAnwer(self) :
        print(self.answer)


if __name__ == "__main__":
    N = int(input())
    C = int(input())
    a = Soluction(N)
    a.inputNode(C)
    a.checkTree(1)
    a.printAnwer()









