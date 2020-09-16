import sys
input = sys.stdin.readline

class Node :
    def __init__(self, data) :
        self.data = data
        self.child = []

class Soluction :
    def __init__(self, N, M, V) :
        self.N = N
        self.M = M
        self.V = V 

        self.reslutBFS = []
        self.reslutDFS = []

        self.checkDFS = [0 for _ in range(self.N+1)]
        self.checkBFS = [0 for _ in range(self.N+1)]
        

        self.nodeDict = dict()
    
    def inputNode(self) :
        for _ in range(self.M) :
            a,b = map(int, input().split(" "))
            if a not in self.nodeDict :
                self.nodeDict[a] = Node(a)
            if b not in self.nodeDict :
                self.nodeDict[b] = Node(b)
            self.nodeDict[a].child.append(b)
            self.nodeDict[b].child.append(a)
    
    def DFS(self, target) :
        self.reslutDFS.append(str(target.data))
        self.checkDFS[target.data] = 1
        target.child = sorted(target.child)
        for i in target.child :
            if self.checkDFS[i] == 0 :
                self.DFS(self.nodeDict[i])
    
    def BFS(self, target) :
        target.child = sorted(target.child)
        temp = []
        for i in target.child :
            if self.checkBFS[i] == 0 :
                self.checkBFS[i] = 1
                self.reslutBFS.append(str(i))
                temp.append(i)
        for i in temp :
            self.BFS(self.nodeDict[i])
    
    def getAnswer(self) :
        self.inputNode()
        self.DFS(self.nodeDict[self.V])

        self.reslutBFS.append(str(self.nodeDict[self.V].data))
        self.checkBFS[self.nodeDict[self.V].data] = 1
        self.BFS(self.nodeDict[self.V])

        print(' '.join(self.reslutDFS))
        print(' '.join(self.reslutBFS))


    

if __name__ == "__main__":
    N,M,V = map(int, input().split(" "))

    t = Soluction(N, M, V)
    t.getAnswer()
    