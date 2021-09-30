import deque from collections
import heapq

class CityInfo :
    def __init__(self,g,s,w,t):
        self.cGold = g
        self.cSilver = s
        self.cWeight = w
        self.cTime = t
        self.canMoveGold = w if g >= w else g
        self.canMoveSilver = w if s >= w else s

class MoveGlodSilver :
    def __init__(self,a,b,g,s,w,t):
        self.gold = a
        self.silver = b
        self.timeHeap = []
        self.timeDict = dict()
        self.makeTimeDict(g,s,w,t)

        self.cityDict = dict()
        self.makeCityDict(g,s,w,t)
    
    def makeCityDict(self, g,s,w,t) :
        for i in range(len(g)) :
            canMoveOne = w[i] if g[i] >= w[i] else g[i]
            # self.cityDict[i] = [g[i], s[i],w[i],t[i], canMoveOne]
            self.cityDict[i] = CityInfo(g[i], s[i],w[i],t[i])
    
    def makeTimeDict(self, g,s,w,t) :
        for i in range(len(t)) :
            newCity = CityInfo(g[i], s[i],w[i],t[i])
            if(t[i] not in self.timeDict) :
                self.timeDict[t[i]] = []
                heapq.heappush(self.timeHeap, t[i])
            self.timeDict[t[i]].append(newCity)

    def makeAnswer(self) :
        while self.timeHeap :
            curTime = heapq.heappop(self.timeHeap)


    def getAnswer(self) :
        gTest = sorted(self.cityDict.items(), key = lambda x: ((self.gold - x[1].canMoveGold), x[1].cTime )   )
        sTest = sorted(self.cityDict.items(), key = lambda x: ((self.gold - x[1].canMoveSilver), x[1].cTime )   )


def solution(a, b, g, s, w, t):
    answer = -1
    mg = MoveGlodSilver(a,b,g,s,w,t)
    mg.getAnswer()    
    print(mg.gold)
    return answer


print(solution(90,500,[70,70,0],[0,0,500],[100,100,2], [4,8,1]))