class Node :
    def __init__(self, data) :
        self.data = data
        self.child = dict()
        self.cnt = 0
class Trie :
    def __init__(self) :
        self.front = Node("")
        self.rear = Node("")
    
    def makeFrontTrie(self, word) :
        self.front.cnt += 1
        if word[0] not in self.front.child :
            self.front.child[word[0]] = Node(word[0])
        target = self.front.child[word[0]]
        target.cnt += 1
        for i in range(1, len(word)) :
            if word[i] not in target.child :
                target.child[word[i]] = Node(word[i])
            target = target.child[word[i]]
            target.cnt += 1
    
    def makeRearTrie(self, word) : 
        self.rear.cnt += 1
        word = word[::-1]
        if word[0] not in self.rear.child :
            self.rear.child[word[0]] = Node(word[0])
        target = self.rear.child[word[0]]
        target.cnt += 1
        for i in range(1, len(word)) :
            if word[i] not in target.child :
                target.child[word[i]] = Node(word[i])
            target = target.child[word[i]]
            target.cnt += 1
    
    def getAnswer(self, quer) :
        if quer[0] == "?" :
            quer = quer[::-1]
            flag = True    
        else : 
            flag = False    

        if flag : 
            target = self.rear
        else :
            target = self.front
        
        for i, v in enumerate(quer) :
            if v == "?" :
                if i == 0 :
                    if flag :
                        return self.rear.cnt
                    else :
                        return self.front.cnt
                return target.cnt
            if v in target.child :
                target = target.child[v]
            else :
                return 0


def solution(words, queries):
    trieDict = dict()
    answer = []
    for i in words :
        if len(i) not in trieDict :
            trieDict[len(i)] = Trie()
        trieDict[len(i)].makeFrontTrie(i)
        trieDict[len(i)].makeRearTrie(i)
    for i in queries :
        if len(i) in trieDict :
            answer.append(trieDict[len(i)].getAnswer(i))
        else :
            answer.append(0)
    

    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["fro??", "?????", "fr???", "fro???", "pro?"] ))