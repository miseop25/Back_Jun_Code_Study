from collections import deque

class Node :
    def __init__(self, num):
        self.val = num
        self.pre = None #노드 클래스 객체 로  들어와야 
        self.next = None
        self.id = -1

class Root :
    def __init__(self, n : Node):
        self.curNode = n
        self.score = 0
        self.preGet = False
        self.doublePre = False
        self.firstCheck = False

def copyRoot(base : Root, target : Root) :
    base.score = target.score
    base.preGet = target.preGet
    base.doublePre = target.doublePre
    base.firstCheck = target.firstCheck
    
class Strcker :
    def __init__(self, sticker):
        self.sticker = sticker
        self.stNode = None
        self.edNode = None
        
        self.nodeDict = dict()
        self.answerArr = []
        self.rootQue = deque([])

    def makeNode(self) :
        totalLen = len(self.sticker) - 1
        for i, val in enumerate(self.sticker) :
            newNode = Node(val)
            newNode.id = i
            
            if i == 0 :
                self.stNode = newNode
            else :
                self.nodeDict[i-1].next = i 
                newNode.pre = i -1 
            if i == totalLen :
                self.edNode = newNode
            
            self.nodeDict[i] = newNode
        self.stNode.pre = self.edNode.id
        self.edNode.next = self.stNode.id

    def makeAnswer(self) :
        firstRootOK = Root(self.stNode)
        firstRootNo = Root(self.stNode)
        firstRootOK.firstCheck = True
        firstRootOK.score += firstRootOK.curNode.val
        firstRootOK.preGet = True

        firstRootNo.curNode = self.nodeDict[self.stNode.next]
        firstRootOK.curNode = self.nodeDict[self.stNode.next]
        rQue = deque()
        rQue.append(firstRootOK)
        rQue.append(firstRootNo)


        while rQue :
            rt = rQue.popleft()
            if rt.curNode.next == self.stNode.id :
                if not rt.firstCheck and not rt.preGet :
                    rt.score += rt.curNode.val
                    self.answerArr.append(rt.score)
                    continue
                else :
                    self.answerArr.append(rt.score)
                    continue

            if rt.preGet == False and rt.doublePre == True :
                ok = Root(rt.curNode)
                copyRoot(ok, rt)
                ok.score += ok.curNode.val
                ok.preGet = True
                ok.doublePre = False
                ok.curNode = self.nodeDict[ok.curNode.next]

                rQue.append(ok)
            elif not rt.preGet :
                ok = Root(rt.curNode)
                no = Root(rt.curNode)
                copyRoot(ok, rt)
                copyRoot(no, rt)
                ok.score += ok.curNode.val
                ok.preGet = True
                ok.curNode = self.nodeDict[ok.curNode.next]
                rQue.append(ok)

                no.doublePre = True
                no.curNode = self.nodeDict[no.curNode.next]
                rQue.append(no)
            else :
                no = Root(rt.curNode)

                copyRoot(no, rt)
                no.doublePre = False
                no.preGet = False
                no.curNode = self.nodeDict[no.curNode.next]
                rQue.append(no)
                
    def getAnswer(self) :
        self.makeNode()
        self.makeAnswer()
        answer = sorted(self.answerArr, reverse= True)
        return answer[0]

            

def solution(sticker):
    answer = 0
    s = Strcker(sticker)
    answer = s.getAnswer()

    return answer

print(solution([14, 6, 5, 11, 3, 9, 2, 10]))