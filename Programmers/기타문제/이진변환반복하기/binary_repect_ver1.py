from collections import deque
class Soluction :
    def __init__(self, s):
        self.count = 0
        self.zeroCnt = 0
        self.s = s
        self.answer = 0
    
    def getAnswer(self) :
        length = len(self.s)
        while length != 1 :
            nowCnt = self.s.count("1")
            self.zeroCnt += length - nowCnt
            self.s = format(nowCnt, 'b')
            length = len(self.s)
            self.count += 1

        return [self.count, self.zeroCnt]


def solution(s):
    answer = []
    s = Soluction(s)
    answer = s.getAnswer()
    return answer