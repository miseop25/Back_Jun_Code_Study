import collections
class PlusCycle :
    def __init__(self, num):
        self.num = num
        self.cnt = 0
    
    def makeNewNum(self, n) :
        buf = ['0', '0']
        if n < 10 :
            buf[0] = '0'
            buf[1] = str(n)
        else :
            temp = list(str(n))
            buf[0] = temp[0]
            buf[1] = temp[1]
        
        plusNum = int(buf[0]) + int(buf[1])
        newNum = collections.deque(list(str(plusNum)))
        if len(newNum) == 2 :
            newNum[0] = buf[1]
        else :
            newNum.appendleft(buf[1])
        
        return int( ''.join(newNum))

    def getAnswer(self) :
        ansNum = self.num
        while True :
            ansNum = self.makeNewNum(ansNum)
            self.cnt += 1 
            if ansNum == self.num :
                return self.cnt


p = PlusCycle(1)
print(p.getAnswer())
        



        