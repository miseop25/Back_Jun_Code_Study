import sys
input = sys.stdin.readline

class Tomato :
    def __init__(self, M,N,H) :
        self.board = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
        self.check = []
        self.answer = 0
        self.count = 0
        self.totalCount = M*N*H

        self.di = [-1,1,0,0,0,0]
        self.dj = [0,0,-1,0,1,0]
        self.dk = [0,0,0,1,0,-1]

        self.M = M
        self.N = N
        self.H = H

    
    def inputTomato(self) :
        for i in range(self.H) :
            for j in range(self.N) :
                t = list(map(int, input().split(" ")))
                for k in range(self.M) :
                    if t[k] == 1 :
                        self.check.append((i,j,k))
                        self.count += 1
                    elif t[k] == -1 :
                        self.totalCount -= 1
                    self.board[i][j][k] = t[k]
    
    def updateTomato(self) :
        newCheck = []
        cnt = self.count
        while self.check :
            i,j,k = self.check.pop()
            for a in range(6) :
                ni = i + self.di[a]
                nj = j + self.dj[a]
                nk = k + self.dk[a]

                if ni < 0 or ni >= self.H or nj < 0 or nj >= self.N or nk < 0 or nk >= self.M :
                    continue
                if self.board[ni][nj][nk] == 0 and self.board[ni][nj][nk] != -1 :
                    self.board[ni][nj][nk] = 1
                    cnt += 1
                    newCheck.append((ni,nj,nk))
        self.check = list(newCheck)
        return cnt

    def getAnswer(self) :
        self.inputTomato()
        while self.count != self.totalCount :
            cnt = self.updateTomato()
            if cnt == self.count :
                return -1
            else :
                self.count = cnt
            self.answer += 1
        return self.answer
        

if __name__ == "__main__":
    M,N,H = map(int, input().split(" "))
    t = Tomato(M,N,H)
    print(t.getAnswer())
