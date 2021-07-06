class Soluction :
    def __init__(self) :
        self.year = int(input())

    def getAnswer(self) :
        if self.year % 4 == 0 and self.year % 100 != 0 :
            return 1 
        elif self.year % 400 == 0 :
            return 1 
        return 0 

if __name__ == "__main__" :
    s = Soluction()
    print(s.getAnswer())