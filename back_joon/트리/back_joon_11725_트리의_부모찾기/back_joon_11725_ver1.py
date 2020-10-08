import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

class Node :
    def __init__(self,data) :
        self.data = data
        self.child = []
        self.parant = None

class Tree :
    def __init__(self, N) :
        self.nodeDict = dict()
        for i in range(1,N+1) :
            self.nodeDict[i] = Node(i)
        self.nodeDict[1].parant = 0
        self.N = N 


    def linkNode(self) :
        for _ in range(self.N-1) :
            a,b = map(int, input().split(" "))
            self.nodeDict[a].child.append(self.nodeDict[b])
            self.nodeDict[b].child.append(self.nodeDict[a])
    
    def findParant(self, target) :
        for i in target.child :
            if i.parant == None :
                i.parant =  target.data 
                self.findParant(i)
    
    def getAnswer(self) :
        self.linkNode()
        self.findParant(self.nodeDict[1])
        result = sorted(self.nodeDict.items(), key= lambda x: x[0])
        for i in result[1: ] :
            print(i[1].parant)


if __name__ == "__main__":
    N = int(input())
    t = Tree(N)
    t.getAnswer()


