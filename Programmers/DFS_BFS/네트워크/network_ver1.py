class Node :
    def __init__(self, data) :
        self.data = data
        self.child = []

class Network :
    def __init__(self, n, computers) :
        self.nodeDict = dict()
        self.n = n
        for i in range(n) :
            self.nodeDict[i] = Node(i)

        self.connectNode(computers)

        self.check = [True for _ in range(n)]

    def connectNode(self, computers) :
        for i in range(self.n) :
            for j in range(self.n) :
                if i == j :
                    continue
                if computers[i][j] == 1:
                    self.nodeDict[i].child.append(j)
    
    def dfsNetwork(self, target) :
        self.check[target.data] = False
        for i in target.child :
            if self.check[i] :
                self.dfsNetwork(self.nodeDict[i])
        
    def getAnswer(self) :
        answer = 0 
        for i in range(self.n) :
            if self.check[i] :
                answer += 1
                self.dfsNetwork(self.nodeDict[i])
        return answer

        
def solution(n, computers):
    answer = 0
    t = Network(n, computers)
    answer = t.getAnswer()
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))