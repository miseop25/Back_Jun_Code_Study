import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

class Soluction :
    def __init__(self, M, N, K) :
        self.board = [[0 for _ in range(M)] for _ in range(N)]
        self.check = [[True for _ in range(M)] for _ in range(N)]
        self.M = M
        self.N = N

        self.warm = []
        self.answer = 0
        self.drawBoard(K)

        self.dy = [0, 1, 0, -1]
        self.dx = [-1, 0, 1, 0]

        
    def drawBoard(self, K) :
        for _ in range(K) :
            x, y = map(int, input().split(" "))
            self.board[y][x] = 1
            self.warm.append([y, x])
    
    def dfs(self, j, i) :
        for k in range(4) :
            x = self.dx[k] + j
            y = self.dy[k] + i
            if x >= 0 and y >= 0 and x < self.N and y < self.M : 
                if self.board[x][y] == 1 and self.check[x][y] :
                    self.check[x][y] = False
                    self.dfs(x,y)
    
    def getAnswer(self) :
        for x,y in self.warm :
            if self.check[x][y] :
                self.check[x][y] = False
                self.answer += 1
                self.dfs(x,y)
        print(self.answer)


if __name__ == "__main__":
    T = int(input())
    for _ in range(T) :
        M,N,K = map(int, input().split(" "))
        a = Soluction(M,N,K)
        a.getAnswer()
