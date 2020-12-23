import sys
input = sys.stdin.readline

class Soluction :
    def __init__(self) :
        self.prePlayTime = 0
        self.nextPlayTime = 0
        self.preDownTime = 0
        self.nextDownTime = 0

        self.song = []
        self.N = 0
    
    def firstInput(self) :
        self.N = int(input())
        for _ in range(self.N) :
            play, down = map(int, input().split(" "))
            self.song.append((play, down))
            self.nextPlayTime += play
            self.nextDownTime += down
    
    def getAnswer(self) :
        for play, down in self.song :
            self.prePlayTime += play
            self.preDownTime += down
            self.nextPlayTime -= play
            self.nextDownTime -= down

            if (self.preDownTime + self.prePlayTime) > self.nextDownTime :
                return self.preDownTime + 1
            elif (self.preDownTime + self.prePlayTime) == self.nextDownTime :
                return self.preDownTime - 1
        return self.preDownTime - 1
s = Soluction()
s.firstInput()
print(s.getAnswer())

    