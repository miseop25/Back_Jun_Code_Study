class SolveProblem :
    def __init__(self, n) :
        self.n = n
        self.board = [[-1 for _ in range(n+1)] for _ in range(n+1) ]

    def installPole(self, x, y) :
        if self.board[x][y] != -1 : return False
        # 바닥일때 기둥
        if y == 0 :
            self.board[x][y] = 0
            return True
        #  보의 한쪽 끝에 설치할때 
        if x > 0 and x < self.n :
            if self.board[x-1][y] == 1 and self.board[x+1][y] != 1 :
                self.board[x][y] = 0
                return True
        # 바로 아래에 기둥이 있을 때
        if self.board[x][y-1] == 0 :
            self.board[x][y] = 0
            return True
        return False
    
    def installPlate(self, x, y) :
        if self.board[x][y] != -1 or y == 0 : return False
        if x < self.n :
            if self.board[x][y-1] == 0 or self.board[x+1][y-1] == 0 :
                self.board[x][y] = 1
                return True
        else :
            if self.board[x][y-1] == 0 :
                self.board[x][y] = 1
                return True
        if x > 0 and x < self.n :
            if self.board[x-1][y] == 1 and self.board[x+1][y] == 1 :
                self.board[x][y] = 1
                return True
        return False

    def delectPole(self, x, y) :
        if y < self.n :
            #  위에가 기둥인 경우
            if self.board[x][y+1] == 0 :
                return False
            else :
            # 위에가 아무것도 없는 경우
                if self.board[x][y+1] == -1 :
                    self.board[x][y] = -1
                    return True
        else :
            self.board[x][y] = -1
            return True

        # 위에 보가 있는 경우
        if self.board[x][y+1] == 1 :
            if x > 0  and  x < self.n  :
                if self.board[x-1][y+1] == 1 and self.board[x+1][y+1] == 1 :
                    self.board[x][y] = -1
                    return True
        elif self.board[x][y+1] == -1 :
            self.board[x][y] = -1
            return True
        return False
    
    def delectPlate(self, x, y) :
        if x > 0 :
            if self.board[x-1][y] == 0 :
                return False
            if self.board[x-1][y] == 1 :
                if self.board[x-1][y-1] != 0 :
                    return False
        if x < self.n :
            if self.board[x+1][y] == 0 :
                return False
            if self.board[x+1][y] == 1 :
                if self.board[x+1][y-1] != 0 :
                    return False
        self.board[x][y] = -1
    
    def getBoardState(self) :
        result = []
        for i in range(self.n+1) :
            for j in range(self.n+1) :
                if self.board[i][j] != -1 :
                    result.append([i,j,self.board[i][j]])
        result = list(sorted(result, key= lambda x: (x[0], x[1],x[2])))
        return result
        
        

def solution(n, build_frame):
    answer = [[]]
    t = SolveProblem(n)
    for x,y,a,b in build_frame :
        if a == 0 :
            if b == 1 :
                t.installPole(x,y)
            else :
                t.delectPole(x,y)
        else :
            if b == 1 :
                t.installPlate(x,y)
            else :
                t.delectPlate(x,y)
    answer = t.getBoardState()
    return answer


print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))
