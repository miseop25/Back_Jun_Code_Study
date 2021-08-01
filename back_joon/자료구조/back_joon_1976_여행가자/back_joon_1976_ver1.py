import sys
from collections import deque
input = sys.stdin.readline

class City :
    def __init__(self,num):
        self.num = num 
        self.bridge = deque([])


class Trip :
    def __init__(self):
        self.N = 0  # City num
        self.M = 0  # Trip City num

        self.cityRootDict = dict()
        self.visited = set()

    def getInput(self) :
        self.N = int(input().rstrip())
        self.M = int(input().rstrip())

        for i in range(1, self.N + 1) :
            self.cityRootDict[i] = City(i)
            buf = list(map(int, input().rstrip().split(" ")))
            for j in range(self.N) :
                if buf[j] or i-1 == j:
                    self.cityRootDict[i].bridge.append(j+1)

    def checkRoot(self) :
        tripRoot = list(map(int, input().rstrip().split(" ")))
        temp = self.cityRootDict[tripRoot[0]].bridge.copy()
        rtSet = set(tripRoot)
        while temp and rtSet :
            st = temp.popleft()
            self.visited.add(st)
            if st in rtSet :
                rtSet.remove(st)
                for i in self.cityRootDict[st].bridge :
                    if i not in self.visited :
                        temp.append(i)

        if len(rtSet) != 0 :
            return "NO"
        else :
            return "YES"


if __name__ == "__main__" :
    t = Trip()
    t.getInput()
    print(t.checkRoot()) 
