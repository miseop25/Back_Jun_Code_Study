import sys
from collections import deque
sys.setrecursionlimit(10**9)
class Node :
    def __init__(self, data) :
        self.data = data
        self.bridge = dict()

class Delivery :
    def __init__(self, N, road, K) :
        self.N = N
        self.road = road
        self.K = K

        self.totalSet = set()
        self.totalSet.add(1)
        self.nodeDict = dict()
        for i in range(1, N+1) :
            self.nodeDict[i] =  [Node(i), 500001]
        self.linkNode(road)

    def linkNode(self, road) :
        for a,b,c in road :
            if b in self.nodeDict[a][0].bridge :
                if self.nodeDict[a][0].bridge[b][1] > c :
                    self.nodeDict[a][0].bridge[b][1] = c 
                    self.nodeDict[b][0].bridge[a][1] = c
            else :
                self.nodeDict[a][0].bridge[b] = [self.nodeDict[b][0], c]
                self.nodeDict[b][0].bridge[a] = [self.nodeDict[a][0], c]
    
    def DFS(self, num, target, dis) :
        for k,v in target.bridge.items()  :
            if dis - v[1] >= 0  :
                if k in self.totalSet :
                    if self.nodeDict[k][1] < dis - v[1] :
                        self.nodeDict[k][1] = dis - v[1]
                        self.DFS(num, v[0], dis - v[1])
                else :
                    self.totalSet.add(k)
                    self.nodeDict[k][1] = dis - v[1]
                    self.DFS(num, v[0], dis - v[1])
    
    

    
    def getAnswer(self):
        answer = 0
        self.DFS(1, self.nodeDict[1][0], self.K)
        answer = len(self.totalSet)
        return answer


    

def solution(N, road, K):
    answer = 0
    d = Delivery(N,road,K)
    answer = d.getAnswer()
    return answer


print(solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4))