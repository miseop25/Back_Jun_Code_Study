class Soluction :
    def __init__(self, word) :
        self.word = word
        self.divisorNum = set()
        self.answer = ''
        self.divisor(len(word))
    
    def divisor(self, num) :
        for i in range(1, int(num**0.5)+1 ) :
            if num%i == 0 :
                self.divisorNum.add(i)
                self.divisorNum.add(num//i)
        self.divisorNum = sorted(self.divisorNum)
    
    def getAnswer(self) :
        n = len(self.divisorNum)//2
        if n == 0 :
            r = 1
            c = 1
        else :
            if self.divisorNum[n]**2 == len(self.word) :
                r = self.divisorNum[n]
            else :
                r = self.divisorNum[n-1]
            c = self.divisorNum[n]
        
        for i in range(r) :
            target = i
            for j in range(c) :
                self.answer += self.word[target]
                target += r
        return self.answer



if __name__ == "__main__":
    word = input().rstrip()
    s = Soluction(word)
    answer= s.getAnswer()
    print(answer)