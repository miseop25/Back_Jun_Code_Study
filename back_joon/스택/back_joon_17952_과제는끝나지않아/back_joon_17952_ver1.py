import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
class HomeWork :
    def __init__(self, score, time):
        self.score = score
        self.time = time

class Soluction :
    def __init__(self, N) :
        self.N = N 
        self.stack = []
        self.target = None
        self.answer = 0
    
    def getAnswer(self) :
        for _ in range(self.N) :
            cmd = list(map(int, input().split(" ")))
            if cmd[0] == 1 :
                self.stack.append(HomeWork(cmd[1], cmd[2]-1))
                self.target = self.stack[-1]
            elif cmd[0] == 0 :
                if self.target != None :
                    self.target.time -= 1 

            if self.target == None :
                continue
            
            elif self.target.time == 0 :
                self.answer += self.target.score
                if self.stack : self.stack.pop()
                if self.stack :
                    self.target = self.stack.pop()
                else :
                    self.target = None
        return self.answer


if __name__ == "__main__":
    N = int(input())
    s = Soluction(N)
    print(s.getAnswer())