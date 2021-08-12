class ScocreBoard :
    def __init__(self, scores):
        self.scores = scores
        self.answer = ""
    
    def getAverge(slef, scoreArr, stNum) :
        sumScore = 0
        scDict = dict()
        scLen = len(scoreArr)
        maxScore = -1
        minScore = 101
        for i, sc in enumerate(scoreArr) :
            if sc > maxScore :
                maxScore = sc
            if sc < minScore :
                minScore = sc
            if sc in scDict :
                scDict[sc].add(i)
            else :
                scDict[sc] = set()
                scDict[sc].add(i)
            sumScore += sc
        
        if scoreArr[stNum] == maxScore :
            if len(scDict[maxScore]) == 1 :
                sumScore -= maxScore
                scLen -= 1
        elif scoreArr[stNum] == minScore :
            if len(scDict[minScore]) == 1 :
                sumScore -= minScore
                scLen -= 1

        return sumScore/scLen
    
    def getGrade(self, score) :
        if score >= 90 :
            return "A"
        elif score >= 80 :
            return "B" 
        elif score >= 70 :
            return "C"
        elif score >= 50 :
            return "D"
        else :
            return "F"

    def getAnswer(self) :
        for i in range(len(self.scores)) :
            scArr = []
            for j in range(len(self.scores)) :
                scArr.append(self.scores[j][i])
            score = self.getAverge(scArr, i) 
            self.answer += self.getGrade(score)
        return self.answer      

def solution(scores):
    answer = ''
    s = ScocreBoard(scores)
    answer = s.getAnswer()
    return answer