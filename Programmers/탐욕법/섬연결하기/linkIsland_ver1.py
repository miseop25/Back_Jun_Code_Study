class Node :
    def __init__(self,data) :
        self.data = data
        self.child = []
        self.price = 0
        self.bridgePrice = 0

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
                    self.nodeDict[i].bridgePrice = p
                    self.dfs(self.nodeDict[i])
            else :
                self.nodeDict[i].price = target.price + p
                self.nodeDict[i].bridgePrice = p
                self.dfs(self.nodeDict[i])
    
    def priceClear(self) :
        for target in self.nodeDict.values():
            target.price = 0
            target.bridgePrice = 0
            self.check = [True for _ in range(len(self.check))]
    

    def getAnswer(self, stNode) :
        self.dfs(self.nodeDict[stNode])
        result = 0
        for target in self.nodeDict.values() :
            result += target.bridgePrice
        return result

    def solution(self) :
        ansList = []
        for i in self.nodeDict.keys() :
            ansList.append(self.getAnswer(i))
            self.priceClear()

        return min(ansList)

def solution(n, costs):
    answer = 0
    t = LinkIsland(n, costs)
    answer = t.solution()
    return answer


print(solution(5,[[0,1,5],[1,2,3],[2,3,3],[3,1,2],[3,0,4],[2,4,6],[4,0,7]] ))