import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

class CheckRGBPlate :
    def __init__(self, N) :
        self.check = [[True for _ in range(N)] for _ in range(N)]
        self.rgCheck = [[True for _ in range(N)] for _ in range(N)]
        self.board = [list(input().rstrip()) for _ in range(N)]
        self.N = N

        self.dx = [0, -1, 0, 1]
        self.dy = [-1, 0, 1, 0]

    def normalDFS(self, i,j, color) :
        for k in range(4) :
            x = self.dx[k] + i
            y = self.dy[k] + j
            if x >=0 and x<self.N and y >= 0 and y < self.N :
                if self.board[x][y] == color and self.check[x][y]:
                    self.check[x][y] = False
                    self.normalDFS(x,y, color)
    
    def rgDFS(self, i,j, color) :
        for k in range(4) :
            x = self.dx[k] + i
            y = self.dy[k] + j
            if x >=0 and x<self.N and y >= 0 and y < self.N :
                if color == "B" :
                    if self.board[x][y] == color and self.rgCheck[x][y]:
                        self.rgCheck[x][y] = False
                        self.rgDFS(x,y, color)
                else :
                    if self.board[x][y] in ["R","G"] and self.rgCheck[x][y] :
                        self.rgCheck[x][y] = False
                        self.rgDFS(x,y, color)

    def getAnswer(self) :
        normal = 0
        rgPerson = 0

        for i in range(self.N) :
            for j in range(self.N) :
                if self.check[i][j] :
                    normal += 1
                    self.check[i][j] = False
                    self.normalDFS(i,j, self.board[i][j])
                if self.rgCheck[i][j] :
                    rgPerson += 1
                    self.rgCheck[i][j] = False
                    self.rgDFS(i,j, self.board[i][j])
        
        return normal, rgPerson
        





if __name__ == "__main__":
    N = int(input())
    t = CheckRGBPlate(N)
    a, b = t.getAnswer()
    print(a, b)
