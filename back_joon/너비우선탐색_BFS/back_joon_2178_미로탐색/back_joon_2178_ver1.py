import sys
from collections import deque
input = sys.stdin.readline


class Maze :
    def __init__(self, N,M, board) :
        self.board = board
        self.check = [[-1 for _ in range(M)] for _ in range(N)]
        self.check[0][0] = 1

        self.M = M
        self.N = N

        self.di = [-1, 0 , 1, 0]
        self.dj = [0, 1, 0, -1]

    def isCorrectIndex(self,i,j) :
        if i >= 0 and i < self.N and j >= 0 and j < self.M :
            return True
        return False

    def DFS(self,i,j) :
        for k in range(4) :
            ni = i + self.di[k]
            nj = j + self.dj[k]
            if not self.isCorrectIndex(ni,nj) :
                continue
            if self.board[ni][nj] == 0 :
                continue
            if self.check[ni][nj] == -1 :
                self.check[ni][nj] = self.check[i][j] + 1
                self.DFS(ni,nj)
            elif self.check[ni][nj] > self.check[i][j] + 1 :
                self.check[ni][nj] = self.check[i][j] + 1
                self.DFS(ni,nj)
        
    def BFS(self, i,j) :
        que = deque([])
        que.append((i,j))
        while que :
            i,j = que.popleft()
            for k in range(4) :
                ni = i + self.di[k]
                nj = j + self.dj[k]
                if not self.isCorrectIndex(ni,nj) :
                    continue
                if self.board[ni][nj] == 0 :
                    continue
                if self.check[ni][nj] == -1 :
                    self.check[ni][nj] = self.check[i][j] + 1
                    que.append((ni,nj))
                elif self.check[ni][nj] > self.check[i][j] + 1 :
                    self.check[ni][nj] = self.check[i][j] + 1
                    que.append((ni,nj))                

    def getAnswer(self) :
        self.BFS(0,0)
        print(self.check[-1][-1])



if __name__ == "__main__":
    N,M = map(int, input().split(" "))
    board = []
    for _ in range(N) :
        word = list(map(int, input().rstrip()))
        board.append(word)
    t = Maze(N,M, board)
    t.getAnswer()