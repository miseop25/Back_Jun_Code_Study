import sys
input = sys.stdin.readline

class Node :
    def __init__(self, data) :
        self.data = data
        self.child = None
        self.parant = None
    

class MakeBigger :
    def __init__(self, N,K,num) :
        self.N = N
        self.K = K
        self.num = num

        self.start = Node(num[0])

        self.makeNode()

    def makeNode(self) :
        target = self.start
        for i in range(1, self.N) :
            target.child = Node(num[i])
            target.child.parant = target
            target = target.child
        
    def getAnswer(self) :
        target = self.start.child
        cnt = 0
        while cnt != self.K :

            if target.data > target.parant.data :
                if target.parant.parant == None :
                    self.start = target
                    target.parant = None
                    target = target.child
                else :
                    target.parant.parant.child = target
                    target.parant = target.parant.parant
                cnt += 1
            else :
                if target.child == None :
                    break
                target = target.child
        
        while cnt != self.K :
            target.parant.child = None
            target = target.parant
            cnt += 1
        
        answer = self.getNumberStatus()
        return answer
    
    def getNumberStatus(self) :
        result = ''
        target = self.start
        while target.child != None :
            result += target.data
            target = target.child
        result += target.data
        return result
        

    



if __name__ == "__main__":
    N, K = map(int, input().split(" "))
    num = list(input().rstrip())
    
    t = MakeBigger(N,K,num)
    print(t.getAnswer())

