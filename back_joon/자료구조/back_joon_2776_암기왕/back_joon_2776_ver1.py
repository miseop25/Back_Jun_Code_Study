import sys
input = sys.stdin.readline

class Soluction :
    def __init__(self) :
        note1 = set()
        note2 = []
    
    def inputInit(self) :
        n = int(input())
        self.note1 = set(map(int, input().split(" ")))
        n2 = int(input())
        self.note2 = list(map(int, input().split(" ")))
    
    def getAnswer(self) :
        self.inputInit()
        for i in self.note2 :
            if i in self.note1 :
                print(1)
            else :
                print(0)

if __name__ == "__main__":
    T = int(input())
    s = Soluction()
    for _ in range(T) :
        s.getAnswer()
