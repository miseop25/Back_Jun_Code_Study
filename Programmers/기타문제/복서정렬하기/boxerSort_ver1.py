class Boxer : 
    def __init__(self, num, myWeight,h2h , boxerWeight):
        self.num = num
        self.weight = myWeight
        self.winRate = 0
        self.overWinCnt = 0

        self.calcWinRate(h2h,boxerWeight)
    
    def calcWinRate(self, h2h, boxerWeight) :
        totalCnt = 0
        winCnt = 0
        for i, cmd in enumerate(h2h) :
            if cmd == "W" :
                winCnt += 1
                if boxerWeight[i] > self.weight :
                    self.overWinCnt += 1
            if cmd != "N" :
                totalCnt += 1
        if totalCnt != 0 and winCnt != 0 :
            self.winRate = (winCnt/totalCnt)*100

class BoxerSort :
    def __init__(self, w, h2h):
        self.boxDict = dict()
        for num, weight in enumerate(w) :
            self.boxDict[num + 1] = Boxer(num, weight, h2h[num], w)
        self.answer = []
    
    def getAnswer(self) :
        dSort = sorted(self.boxDict.items(), key = lambda x: (-x[1].winRate, -x[1].overWinCnt, -x[1].weight, x[0])  )
        for i in dSort :
            self.answer.append(i[0])
        return self.answer            

def solution(weights, head2head):
    answer = []
    bs = BoxerSort(weights,head2head)
    answer = bs.getAnswer()
    return answer

print(solution([50, 82, 75, 120],["NLWL", "WNLL", "LWNW", "WWLN"] ))