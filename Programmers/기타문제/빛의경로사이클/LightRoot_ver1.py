top = (0,-1)
bottom = (0,1)
left = (1,0)
right = (-1,0)

class CycleInfo :
    def __init__(self, x, y, dir):
        self.startInfo = (x,y,dir)
        self.curX = x 
        self.curY = y
        self.curDir = dir
        self.dist = 0

class LightCycle :
    def __init__(self, grid):
        self.board = []
        self.makeBoard(grid)
        self.xLen = len(grid[0])
        self.yLen = len(grid)

        self.vistedSet = set()
        self.answer = []

    def makeBoard(self, grid) :
        for g in grid :
            self.board.append(list(g))
    
    def outOfRangeCheck(self, cInfo : CycleInfo) -> CycleInfo :
        if cInfo.curX >= self.xLen :
            cInfo.curX = 0
        elif cInfo.curX < 0 :
            cInfo.curX = self.xLen - 1

        if cInfo.curY >= self.yLen :
            cInfo.curY = 0
        elif cInfo.curY < 0 :
            cInfo.curY = self.yLen - 1
        return cInfo
    
    def cmdS(self, cInfo : CycleInfo) :
        x,y = cInfo.curDir
        cInfo.curX += x 
        cInfo.curY += y
        cInfo = self.outOfRangeCheck(cInfo)
        cInfo.dist += 1
        vist = (cInfo.curX, cInfo.curY, cInfo.curDir)
        self.vistedSet.add(vist)

    def cmdR(self, cInfo : CycleInfo) :
        if cInfo.curDir == top :
            cInfo.curDir = right
        elif cInfo.curDir == bottom :
            cInfo.curDir = left
        elif cInfo.curDir == right :
            cInfo.curDir = bottom
        elif cInfo.curDir == left :
            cInfo.curDir = top

        self.cmdS(cInfo)
    
    def cmdL(self, cInfo : CycleInfo) :
        if cInfo.curDir == top :
            cInfo.curDir = left
        elif cInfo.curDir == bottom :
            cInfo.curDir = right
        elif cInfo.curDir == right :
            cInfo.curDir = top
        elif cInfo.curDir == left :
            cInfo.curDir = bottom

        self.cmdS(cInfo)


    def doCycle(self, cInfo : CycleInfo) :
        while (True) :
            cmd = self.board[cInfo.curY][cInfo.curX]
            if cInfo.startInfo == (cInfo.curX, cInfo.curY, cInfo.curDir) :
                self.answer.append(cInfo.dist)
                return
            if cmd == "S" :
                self.cmdS(cInfo)
            elif cmd == "L" :
                self.cmdL(cInfo)
            elif cmd == "R" :
                self.cmdR(cInfo)
        
    def makeAnswer(self) :
        for i in range(self.yLen)  :
            for j in range(self.xLen) :
                for dir in [top, bottom, left, right] :
                    if (j, i, dir) in self.vistedSet :
                        continue
                    cInfo = CycleInfo(j,i, dir)
                    self.vistedSet.add(cInfo.startInfo)
                    self.cmdS(cInfo)
                    self.doCycle(cInfo)
        self.answer = sorted(self.answer)
        return self.answer


def solution(grid):
    answer = []
    lc = LightCycle(grid)
    answer = lc.makeAnswer()
    return answer

print(solution(["R","R"]))