class CellInfo :
    def __init__(self, num):
        self.myNum = num
        self.next = -1 
        self.pre = -1

class Table :
    def __init__(self,n,k,cmd):
        self.n = n
        self.curTable = k
        self.cmds = cmd 
        self.tableDict = dict()
        self.delTable =[]
        self.makeTableList()
    
    def makeTableList(self) :
        for i in range(self.n) :
            self.tableDict[i] = CellInfo(i)
            if i != 0 :
                self.tableDict[i-1].next = i
                self.tableDict[i].pre = i-1
    
    def moveCell(self,cmd, cnt) :
        # while cnt > 0 :
        for _ in range(cnt) :
            now = self.tableDict[self.curTable]
            if cmd == "D" :
                if now.next == -1 :
                    return
                self.curTable = now.next
                cnt -= 1
            elif cmd == "U" :
                if now.pre == -1 :
                    return
                self.curTable = now.pre
                cnt -= 1
            
    def delectCell(self) :
        preCell = self.tableDict[self.curTable].pre
        nextCell = self.tableDict[self.curTable].next
        # self.delTable.append(self.tableDict[self.curTable])
        self.delTable.append(self.curTable)

        if preCell != -1 :
            self.tableDict[preCell].next = nextCell
        if nextCell != -1 :
            self.tableDict[nextCell].pre = preCell
            self.curTable = nextCell
        else :
            self.curTable = preCell
    
    def undoCmd(self) :
        if not self.delTable :
            return
        uc = self.delTable.pop()
        uCell = self.tableDict[uc]
        if uCell.pre != -1 :
            nextCell = self.tableDict[uCell.pre].next    
            self.tableDict[uCell.pre].next = uCell.myNum
            self.tableDict[uc].next = nextCell
        if self.tableDict[uc].next != -1 :
            self.tableDict[uCell.next].pre = uCell.myNum 


    def doCmd(self) :
        for c in self.cmds :
            cmd = ''
            cnt = 0
            if len(c) == 3 :
                cmd, cnt = c.split(" ")
            else :
                cmd = c 

            if cmd == "C" :
                self.delectCell()
            elif cmd == "Z" :
                self.undoCmd()
            else :
                self.moveCell(cmd,int(cnt))

    def getAnswer(self) :
        self.doCmd()
        answer = ''
        while self.delTable :
            d = self.delTable.pop()
            if d in self.tableDict :
                del self.tableDict[d]
        for i in range(self.n) :
            if i in self.tableDict :
                answer += "O"
            else :
                answer += "X"
        return answer
            

def solution(n, k, cmd):
    answer = ''
    t = Table(n,k,cmd)
    answer = t.getAnswer()
    return answer

n = 8
k = 2
cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
print(solution(n,k,cmd))