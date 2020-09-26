class Node :
    def __init__(self,data) :
        self.data = data
        self.child = []
        self.price = 0

class LinkIsland :
    def __init__(self,n,costs) :
        self.nodeDict = dict()
        for i in range(n) :
            self.nodeDict[i] = Node(i)
        self.check = [True for _ in range(n)]
        self.makeBridge(costs)
        
    def makeBridge(self, cost) :
        for a, b, c in cost :
            self.nodeDict[a].child.append([b, c])
            self.nodeDict[b].child.append([a, c])
    
    def dfs(self, target) :
        self.check[target.data] = False
        for i,p in target.child :
            if self.check[i] == False :
                if self.nodeDict[i].price > target.price + p :
                    self.nodeDict[i].price = target.price + p
                    self.dfs(self.nodeDict[i])
            else :
                self.nodeDict[i].price = target.price + p
                self.dfs(self.nodeDict[i])
    

    def getAnswer(self) :
        self.dfs(self.nodeDict[0])
        result = -1
        for target in self.nodeDict.values() :
            result += target.price
        return result




def solution(n, costs):
    answer = 0
    t = LinkIsland(n, costs)
    answer = t.getAnswer()
    return answer


print(solution(4,[[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]] ))