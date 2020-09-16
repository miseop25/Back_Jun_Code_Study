import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**8)


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
        for i in range(1, N +1 ) :
            self.nodeDict[i] = Node(i)
    
    def inputNode(self) :
        for _ in range(self.M) :
            a,b = map(int, input().split(" "))
            self.nodeDict[a].child.append(b)
            self.nodeDict[b].child.append(a)
    
    def DFS(self, target) :
        self.reslutDFS.append(str(target.data))
        self.checkDFS[target.data] = 1
        target.child = sorted(target.child)
        for i in target.child :
            if self.checkDFS[i] == 0 :
                self.DFS(self.nodeDict[i])

    def DFS_Use_Stack(self, target) :
        stack = []
        checkRoot = [0 for _ in range(self.N+1)]
        result = []
        stack.append(target.data) 
        checkRoot[target.data] = 1
        result.append(target.data)

        while stack :
            target.child = sorted(target.child)
            flag = True
            for i in target.child :
                if checkRoot[i] == 0 :
                    target = self.nodeDict[i]
                    stack.append(target.data)
                    result.append(i)
                    checkRoot[i] = 1
                    flag = False
                    break
            if flag :
                target = self.nodeDict[stack.pop()]
        return result

        
        
    
    def BFS(self, target) :
        que = deque([])
        que.append(target)
        self.checkBFS[target.data] = 1
        while que :
            n = que.popleft()
            self.reslutBFS.append(str(n.data))
            c = sorted(n.child)
            for i in c :
                if self.checkBFS[i] == 0 :
                    que.append(self.nodeDict[i])
                    self.checkBFS[i] = 1
    
    def getAnswer(self) :
        self.inputNode()
        self.DFS(self.nodeDict[self.V])
        self.BFS(self.nodeDict[self.V])
        print(' '.join(self.reslutDFS))
        print("DFS_use_Stack : ", self.DFS_Use_Stack(self.nodeDict[self.V]))
        print(' '.join(self.reslutBFS))


    

if __name__ == "__main__":
    N,M,V = map(int, input().split(" "))
    t = Soluction(N, M, V)
    t.getAnswer()
    