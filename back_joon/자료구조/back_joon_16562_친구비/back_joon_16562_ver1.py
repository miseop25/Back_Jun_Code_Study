import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000000)

class Node :
    def __init__(self, data) :
        self.data = data
        self.child = set()

class FriendMoney :
    def __init__(self) :
        self.N, self.M, self.K = map(int, input().rstrip().split(" "))
        self.money = list(map(int, input().rstrip().split(" ")))
        self.friendDict = dict()
        for i in range(1, self.N+1) :
            self.friendDict[i] = Node(i)
        self.bfs = [0 for i in range(self.N+1)]
    
    def inputFriendRelation(self) :
        for _ in range(self.M) :
            a, b = map(int, input().split(" "))
            self.friendDict[b].child.add(self.friendDict[a])
            self.friendDict[a].child.add(self.friendDict[b])
    
    def checkFriends(self,temp,value) :
        result = value
        self.bfs[temp.data] = 1
        for i in temp.child :
            if self.bfs[i.data] == 1 :
                continue
            comp = self.checkFriends(i, result)
            if comp < result :
                result = comp
        return result
    
    def soluction(self) :
        total = self.K
        for i in range(1, 1+self.N) :
            if self.bfs[i] == 0 :
                pay = self.checkFriends(self.friendDict[i], self.money[i-1])
                total -= pay
                if total < 0 :
                    return "Oh no"
        return self.K - total

if __name__ == "__main__":
    s = FriendMoney()
    s.inputFriendRelation()
    print(s.soluction())
