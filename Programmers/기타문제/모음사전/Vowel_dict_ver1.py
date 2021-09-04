class Vowel :
    def __init__(self):
        self.num = 1
        self.wordDict = dict()
        self.baseWord = ['A', 'E','I','O','U']
    
    def makeWord(self, target) :
        for i, v in enumerate(self.baseWord) :
            temp = target + v
            if len(temp) < 6 :
                self.wordDict[temp] = self.num
                self.num += 1
                self.makeWord(temp)
            else :
                break


def solution(word):
    answer = 0
    v = Vowel()
    v.makeWord('')
    answer = v.wordDict[word]
    return answer

print(solution("EIO"))