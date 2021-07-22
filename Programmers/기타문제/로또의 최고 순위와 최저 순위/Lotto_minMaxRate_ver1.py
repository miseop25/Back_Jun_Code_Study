class Lotto :
    def __init__(self, lottos, winNum):
        self.lottos = lottos
        self.winNum = set(winNum)
        self.answer = [7,7]
    
    def checkLotto(self) :
        for i in self.lottos :
            if i == 0 :
                self.answer[0] -= 1
            if i in self.winNum :
                self.answer[1] -= 1
                self.answer[0] -= 1

        if self.answer[0] == 7 :
            self.answer[0] = 6
        if self.answer[1] == 7 :
            self.answer[1] = 6




def solution(lottos, win_nums):
    answer = []
    l = Lotto(lottos,win_nums)
    l.checkLotto()
    answer = l.answer
    return answer


