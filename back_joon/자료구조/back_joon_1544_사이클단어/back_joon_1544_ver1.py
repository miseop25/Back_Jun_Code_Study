import collections

class Soluction :
    def __init__(self):
        self.N = 0
        self.wordDict = dict() 

    def getFirstInput(self) :
        self.N = int(input())
    
    def isInWordDict(self, word) :
        l = len(word) 
        temp = collections.deque(list(word))
        for _ in range(l) :
            buf = ''.join(temp)
            if buf in self.wordDict :
                self.wordDict[buf] += 1
                return True
            a = temp.popleft()
            temp.append(a)
        return False


if __name__ == "__main__" :
    s = Soluction()
    s.getFirstInput()
    for _ in range(s.N) :
        word = input().rstrip()
        if not s.isInWordDict(word) :
            s.wordDict[word] = 1 
    
    print(len(s.wordDict))


