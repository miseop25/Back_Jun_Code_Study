class MoveGlodSilver :
    def __init__(self,a,b,g,s,w,t):
        self.gold = a
        self.silver = b

        self.cityDict = dict()
        self.makeCityDict(g,s,w,t)
    
    def makeCityDict(self, g,s,w,t) :
        for i in range(len(g)) :
            canMoveOne = w[i] if g[i] >= w[i] else g[i]
            self.cityDict[i] = [g[i], s[i],w[i],t[i], canMoveOne]


def solution(a, b, g, s, w, t):
    answer = -1
    return answer