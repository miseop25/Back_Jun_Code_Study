import sys
from collections import deque
input = sys.stdin.readline

class Soluction :
    def __init__(self, N,M) :
        self.N = N
        self.M = M

        self.personDict = dict()
        self.partyDict = dict()
        self.partyPerson = dict()

        self.check = [True]*(N+1)
        self.stack = deque([])
    
    def initData(self) :
        for i in range(1,self.N+1) :
            self.personDict[i] = set()
        for i in range(1, self.M + 1) :
            self.partyDict[i] = True
            self.partyPerson[i] = []
        
        knows = list(map(int, input().split(" ")))
        for k in range(1, len(knows)) :
            self.stack.append(knows[k])
        
        for i in range(1, self.M+1) :
            party = list(map(int, input().split(" ")))
            for j in range(1,party[0]+1) :
                self.personDict[party[j]].add(i)
                self.partyPerson[i].append(party[j])
    
    def checkParty(self) :
        while(self.stack) :
            temp = self.stack.popleft()
            if self.check[temp] :
                self.check[temp] = False
                for k in self.personDict[temp] :
                    self.partyDict[k] = False
                    for c in self.partyPerson[k] :
                        if self.check[c] :
                            self.stack.append(c)
    
    def getAnswer(self) :
        self.initData()
        self.checkParty()
        answer = 0 
        for k,v in self.partyDict.items() :
            if v :
                answer += 1
        return answer



if __name__ == "__main__":
    N, M = map(int, input().split(" "))
    s = Soluction(N,M)
    answer = s.getAnswer()
    print(answer)

     