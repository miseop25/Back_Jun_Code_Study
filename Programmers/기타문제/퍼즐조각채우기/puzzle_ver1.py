from collections import deque

class PieceInfo :
    def __init__(self, num, locaArr):
        self.num = num
        self.loca = locaArr

class PuzzleGame :
    def __init__(self, gameBoard, table):
        self.answer = 0
        self.gameBoard = gameBoard
        self.table = table 
        self.N = len(gameBoard)

        self.gmaeDict = dict()
        self.tableDict = dict()

        self.gameVisted = set()
        self.tableVisted = set()

        self.dx = [-1,0,1,0]
        self.dy = [0,1,0,-1]

    def findPiece(self, target, board, x, y, visted) :
        visted.add((x,y)) 
        que = deque([(x,y)])
        arr = [(x,y)]
        while que :
            qx, qy = que.popleft()
            for i in range(4) :
                nx = qx + self.dx[i]
                ny = qy + self.dy[i]
                if nx < 0 or nx >= self.N or ny < 0 or ny >= self.N :
                    continue
                if board[nx][ny] != target :
                    continue
                if (nx,ny) in visted :
                    continue
                visted.add((nx, ny))
                que.append((nx, ny))
                arr.append((nx,ny))
        return arr
    
    def getTablePiece(self) :
        for i in range(self.N) :
            for j in range(self.N) :
                if (i,j) in self.tableVisted or self.table[i][j] == 0:
                    continue
                arr = self.findPiece(1, self.table, i,j, self.tableVisted)
                newPiece = PieceInfo(len(arr), arr)
                if len(arr) not in self.tableDict: 
                    self.tableDict[len(arr)] = deque([])
                self.tableDict[len(arr)].append(newPiece)
    
    def getBoardPiece(self) :
        for i in range(self.N) :
            for j in range(self.N) :
                if (i,j) in self.gameVisted or self.gameBoard[i][j] == 1:
                    continue
                arr = self.findPiece(0, self.gameBoard, i,j, self.gameVisted)
                newPiece = PieceInfo(len(arr), arr)
                if len(arr) not in self.gmaeDict: 
                    self.gmaeDict[len(arr)] = deque([])
                self.gmaeDict[len(arr)].append(newPiece)
    
    def moveToZero(self, arr) :
        result = []
        leftArr = sorted(arr, key = lambda x : x[0])
        topArr = sorted(arr, key = lambda x: x[1])

        left = leftArr[0][0]
        top = topArr[0][1]

        for x,y in arr :
            result.append((x-left, y - top))
        
        return sorted(result)

    def rotate90(self, arr) :
        retsut = []
        for x ,y in arr :
            if y == 0  :
                retsut.append((y, self.N-1 -y - x))
            elif x == 0 : 
                retsut.append((y, self.N -1 ))
            else :
                retsut.append((y, self.N-1 - y))
        return self.moveToZero(retsut)

        

    def getAnswer(self) :
        self.getBoardPiece()
        self.getTablePiece()  
        for k in self.gmaeDict.keys() :
            if k not in self.tableDict :
                continue
            if k == 2 : 
                self.answer += min(len(self.gmaeDict[k]), len(self.tableDict[k]))*2
                continue
            elif k == 1 :
                self.answer += min(len(self.gmaeDict[k]), len(self.tableDict[k]))
                continue

            while self.gmaeDict[k] :
                piece = self.gmaeDict[k].pop()
                piece.loca = self.moveToZero(piece.loca)
                bf = False
                for tp in self.tableDict[k] :
                    target = self.moveToZero(tp.loca)
                    for _ in range(4) : 
                        if target == piece.loca :
                            self.answer += k
                            bf = True
                            break
                        else :
                            target = self.rotate90(target)

        
        return self.answer
                    
            

def solution(game_board, table):
    answer = -1
    g = PuzzleGame(game_board, table)
    answer = g.getAnswer()
    return answer


gameBoard = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]	
table = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]	
print(solution(gameBoard, table))
