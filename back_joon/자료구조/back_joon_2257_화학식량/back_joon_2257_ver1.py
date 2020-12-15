import sys
input = sys.stdin.readline

class Soluction :
    def __init__(self, word):
        self.word = word

        self.stack = []
        self.total = []

        self.chemDict = {"H":1, "C": 12, "O":16}
    
    def getAnswer(self) :
        for i in self.word :
            if i == "(" :
                self.stack.append([])
                continue
            elif i == ")" :
                temp = self.stack.pop()
                if self.stack :
                    self.stack[-1].append(sum(temp))
                else : 
                    self.total.append(sum(temp))
                    
                continue
            
            try:
                cnt = int(i)
                if self.stack :
                    self.stack[-1][-1] = self.stack[-1][-1] * cnt
                else :
                    self.total[-1] = self.total[-1] * cnt
            except :
                if self.stack :
                    self.stack[-1].append(self.chemDict[i])
                else :
                    self.total.append(self.chemDict[i])
        
        return sum(self.total)

if __name__ == "__main__":
    word = input().rstrip()
    s = Soluction(word)
    print(s.getAnswer())