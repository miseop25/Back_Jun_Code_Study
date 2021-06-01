class SelfNumber :
    def __init__(self):
        self.num = set([i for i in range(1, 10001)])
    
    def makeSelfNumber(self) :
        for i in range(1, 10001) :
            target = i
            for p in str(i) :
                target += int(p)

            if target in self.num :
                self.num.remove(target)
    
    def getAnswer(self) :
        for i in self.num :
            print(i)


if __name__ == "__main__" :
    s = SelfNumber()
    s.makeSelfNumber()
    s.getAnswer()

