from collections import deque

class NumString :
    def __init__(self, s):
        self.word = deque(list(s))
        self.answer = ''
        self.numDict = dict()

    def makeNumDict(self) :
        self.numDict["zero"] = "0"
        self.numDict["one"] = "1"
        self.numDict["two"] = "2"
        self.numDict["three"] = "3"
        self.numDict["four"] = "4"
        self.numDict["five"] = "5"
        self.numDict["six"] = "6"
        self.numDict["seven"] = "7"
        self.numDict["eight"] = "8"
        self.numDict["nine"] = "9"

    def makeNumStrToNum(self) :
        bufword = ""
        while self.word :
            char = self.word.popleft()
            if char >= '0' and char <= '9' :
                self.answer += char
            else :
                bufword += char
                
            if bufword in self.numDict :
                self.answer += self.numDict[bufword]
                bufword = ""
    def getAnswer(self) :
        self.makeNumDict()
        self.makeNumStrToNum()
        return int(self.answer)


def solution(s):
    answer = 0
    a = NumString(s)
    answer = a.getAnswer()
    return answer

if __name__ == "__main__" :
    print(solution("one4seveneight"))