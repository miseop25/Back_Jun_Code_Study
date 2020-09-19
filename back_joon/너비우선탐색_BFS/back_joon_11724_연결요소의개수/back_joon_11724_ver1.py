import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

class Node :
    def __init__(self, data) :
        self.data = data
        self.linked = []

class ConnectedComponent :
    def __init__(self, N, M) :
        self.nodeDict = dict()
        for i in range(1, N+1) :
            self.nodeDict[i] = Node(i)
        
        self.check = [True for _ in range(N+1)]
        self.M = M

    def inputNode(self) :
        for _ in range(self.M) :
            a,b = map(int, input().split(" "))
            self.nodeDict[a].linked.append(b)
            self.nodeDict[b].linked.append(a)
    
    def dfs(self, target) :
        self.check[target.data] = False 
        for i in target.linked :
            if self.check[i] :
                self.dfs(self.nodeDict[i])
    
    def getAnswer(self) :
        answer = 0
        self.inputNode()
        for i in range(1, len(self.check)) :
            if self.check[i] :
                answer += 1 
                self.dfs(self.nodeDict[i])
        print(answer)




if __name__ == "__main__":
    N, M = map(int, input().split(" "))
    a = ConnectedComponent(N, M)
    a.getAnswer()
