class CheckDist :
    def __init__(self, places):
        self.places = places

        self.person = []
        self.UDRL = [(-1,0), (1,0), (0,1), (0,-1)]
        self.XPos = [(-1,-1), (-1,1), (1,-1), (1,1)]
        self.XPosOpt = [ 
            [(-1,0), (0,-1) ],
            [(-1,0), (0,1)],
            [(0,1), (1,0)],
            [(1,0), (0,-1)]
        ]

    def checkPerson(self) :
        for i in range(5) :
            l = list(self.places[i])
            for j in range(5) :
                if l[j] == "P" :
                    self.person.append((i,j))

    def checkCase1(self, x, y) -> bool :
        for i in range(4) :
            nx = x + self.UDRL[i][0]
            ny = y + self.UDRL[i][1]
            if nx < 0 or nx > 4 or ny < 0 or ny > 4 :
                continue
            if self.places[nx][ny] == "P" :
                return False
        return True
    
    def checkCase2(self, x, y) -> bool :
        for i in range(4) :
            nx = x + self.UDRL[i][0]*2
            ny = y + self.UDRL[i][1]*2

            ex = x + self.UDRL[i][0]
            ey = y + self.UDRL[i][1]
            if nx < 0 or nx > 4 or ny < 0 or ny > 4 :
                continue
            if self.places[nx][ny] == "P" and self.places[ex][ey] != "X":
                return False
        return True

    def checkCase3(self, x, y) -> bool :
        for i in range(4) :
            nx = x + self.XPos[i][0]
            ny = y + self.XPos[i][1]
            opt1 = self.XPosOpt[i][0]
            opt2 = self.XPosOpt[i][1]
            
            ex1 = opt1[0] + x
            ey1 = opt1[1] + y
            ex2 = opt2[0] + x
            ey2 = opt2[1] + y

            if nx < 0 or nx > 4 or ny < 0 or ny > 4  :
                continue
            if ex1 < 0 or ex1 > 4 or ey1 < 0 or ey1 > 4  :
                continue
            if ex2 < 0 or ex2 > 4 or ey2 < 0 or ey2 > 4  :
                continue
            if self.places[nx][ny] == "P" and self.places[ex1][ey1] != "X" and self.places[ex2][ey2] != "X" :
                return False
        return True
    
    def getAnswer(self) :
        self.checkPerson()
        for x,y in self.person :
            if not self.checkCase1(x,y) or not self.checkCase2(x,y) or not self.checkCase3(x,y) :
                return 0
        return 1 


def solution(places):
    answer = []
    for i in places :
        c = CheckDist(i)
        answer.append(c.getAnswer())
    return answer

p = [["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(p))