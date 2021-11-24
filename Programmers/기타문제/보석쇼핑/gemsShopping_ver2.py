class Gem :
    def __init__(self, gems):
        self.gems = gems
        self.gemDict = dict() 
        self.gemsSet = set(gems)
        self.gLen = len(self.gemsSet)

        self.answer = []

    def makeAnswer(self) :
        flag = True #구간을 줄일지 말지 True : 구간 늘리는것, False 구간 줄이기
        i = 0 
        j = 0

        while j < len(self.gems) or not flag :
            if flag :
                targetGems = self.gems[j]
                if targetGems not in self.gemDict :
                    self.gemDict[targetGems] = 1 # 현재 구간에 보석 추가
                else :
                    self.gemDict[targetGems] += 1
                j += 1
            else :
                targetGems = self.gems[i]
                self.gemDict[targetGems] -= 1 
                if(self.gemDict[targetGems] == 0) :
                    self.gemDict.pop(targetGems)
                i += 1

            if len(self.gemDict) == self.gLen :
                flag = False #현재 구간의 보석의 개수와 전체 보석의 개수가 같다면!
                self.answer.append([i+1, j])
            else :
                flag = True
    
    def getAnswer(self) :
        self.makeAnswer()
        result = sorted(self.answer, key= lambda x: (x[1]-x[0], x[0]))
        return result[0]




def solution(gems):
    answer = []
    g = Gem(gems)
    answer = g.getAnswer()
    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["a", "a", "b"]))