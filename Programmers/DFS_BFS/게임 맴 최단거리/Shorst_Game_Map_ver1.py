import sys
from collections import deque

class Soluction :
    def __init__(self, maps) :
        self.maps = maps
        self.check = []
        self.n = len(maps)
        self.m = len(maps[0])
        self.dx = [0,0,-1,1]
        self.dy = [-1,1,0,0]
        self.position = deque()
        
    def initCheck(self) :
        for i in range(self.n) :
            temp = []
            for j in range(self.m) :
                temp.append(0)
            self.check.append(temp)

    def isCorrectIndex(self,i,j) :
        if i >= 0 and i < self.n and j >= 0 and j < self.m :
            return True
        return False


    def BFS(self, a,b) :
        self.position.append([a,b])
        while self.position :
            i,j = self.position.popleft()
            for k in range(4) :
                nx = i + self.dx[k]
                ny = j + self.dy[k]
                if not self.isCorrectIndex(nx,ny) :
                    continue
                
                if self.maps[nx][ny] == 0 :
                    continue

                if self.check[nx][ny] == 0 :
                    self.check[nx][ny] = self.check[i][j] + 1
                    self.position.append([nx,ny])
                elif self.check[nx][ny] > self.check[i][j] + 1 :
                    self.check[nx][ny] = self.check[i][j] + 1 
                    self.position.append([nx,ny])

    def getAnswer(self) :
        self.initCheck()
        self.BFS(0,0)
        return self.check[-1][-1]


def solution(maps):
    s = Soluction(maps)
    answer = s.getAnswer() 
    if answer :
        answer += 1
    else :
        answer -=1 
    return answer


solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])