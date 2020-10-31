import sys
input = sys.stdin.readline

class Soluction :
    def __init__(self) :
        self.board = [[0 for _ in range(5)] for _ in range(5)]
        self.numDict = dict()
        self.masterBoard = []
    
    def myBoardInput(self) :
        for i in range(5) :
            num = list(map(int, input().split(" ")))
            for j in range(5) :
                self.numDict[num[j]] = (i,j)
    
    def masterBoardInput(self) :
        for _ in range(5) :
            self.masterBoard.append(list(map(int, input().split(" "))))

    def checkBingo(self) :
        cnt = 0
        # 가로줄 확인하기
        for i in range(5) :
            if sum(self.board[i]) == 5 :
                cnt += 1
        # 세로줄 확인하기
        for j in range(5) :
            temp = 0
            for i in range(5) :
                temp += self.board[i][j]
            if temp == 5 :
                cnt += 1
        
        # 대각선 확인하기 
        temp = 0
        nTemp = 0
        i = 0
        j = 0
        nj = 4
        for _ in range(5) :
            temp += self.board[i][j]
            nTemp += self.board[i][nj]
            i += 1
            j += 1
            nj -= 1
        if temp == 5 :
            cnt += 1
        if nTemp == 5 :
            cnt += 1

        if cnt >=3 :
            return True
        else :
            return False


    def getAnswer(self):
        self.myBoardInput()
        self.masterBoardInput()
        cnt = 0 
        for i in range(5) :
            for j in range(5) :
                x, y= self.numDict[self.masterBoard[i][j]]
                self.board[x][y] = 1
                cnt += 1
                if self.checkBingo() :
                    return cnt





if __name__ == "__main__":
    answer = 0
    t= Soluction()
    answer = t.getAnswer()
    print(answer)