import sys
sys.setrecursionlimit(10**7)
class Soluction :
    def __init__(self, board) :
        self.board = board
        self.answer = [0,0]
    
    def checkBoard(self, a, b ,c, d) :

        half = (a+b)//2
        case = [[a, half, a, half], [a, half, half, b], [half , b, half, b], [half, b, a, half]]
        for i in case :
            a = i[0]
            b = i[1]
            c = i[2]
            d = i[3]
            flag = True
            st = self.board[a][c]
            if a == b or c == d :
                self.answer[self.board[a][b]] += 1
                continue
            for j in range(a, b) :
                for k in range(c,d) :
                    if self.board[j][k] != st :
                        self.checkBoard(a,b,c,d)
                        flag = False
                        break
                if flag :
                    break
            if flag :
                self.answer[st] += 1
    
    def getAnswer(self) :
        M = len(self.board)
        self.checkBoard(0,M,0,M)
        return [self.answer[0], self.answer[1]]

def solution(arr):
    answer = []
    t = Soluction(arr)
    answer = t.getAnswer()
    return answer


print(solution([[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]))