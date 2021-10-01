from collections import deque

class NumInfo :
    def __init__(self, num):
        self.myNum = num
        self.cnt = 0

class InAndOut :
    def __init__(self, enter, leave):
        self.enter = deque(enter)
        self.leave = deque(leave)
        self.totalLen = len(enter)

        self.nDict = dict()
        self.ansDict = dict()
    
    def makeAnswer(self) :
        while self.leave :
            target = self.leave.popleft()
            n = -1
            while target not in self.nDict :
                self.plusNumCnt()
                n = self.enter.popleft()
                newNum = NumInfo(n)
                newNum.cnt = len(self.nDict)
                self.nDict[n] = newNum
            self.ansDict[target] = self.nDict[target]
            del self.nDict[target]
        answer = []
        for i in range(1, (self.totalLen) + 1) :
            answer.append(self.ansDict[i].cnt)
        return answer
    
    def plusNumCnt(self) :
        for k in self.nDict.keys() :
            self.nDict[k].cnt += 1


def solution(enter, leave):
    answer = []
    s = InAndOut(enter,leave)
    answer = s.makeAnswer()
    return answer