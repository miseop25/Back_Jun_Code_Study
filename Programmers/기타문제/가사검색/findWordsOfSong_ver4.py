class Node :
    def __init__(self, data) :
        self.data = data
        self.child = dict()
class Trie :
    def __init__(self, array) :
        self.front = Node("")
        self.rear = Node("")
        self.wordArray = array
    
    def makeFrontTrie(self) :
        for word in self.wordArray :
            if word[0] not in self.front.child :
                self.front.child[word[0]] = Node(word[0])
            target = self.front.child[word[0]]
            for i in range(1, len(word)) :
                if word[i] not in target.child :
                    target.child[word[i]] = Node(word[i])
                target = target.child[word[i]]
    
    def makeRearTrie(self) : 
        for word in self.wordArray :
            word = word[::-1]
            if word[0] not in self.rear.child :
                self.rear.child[word[0]] = Node(word[0])
            target = self.rear.child[word[0]]
            for i in range(1, len(word)) :
                if word[i] not in target.child :
                    target.child[word[i]] = Node(word[i])
                target = target.child[word[i]]
    
    def checkLeaf(self, present, cnt, result) :
        current = result
        if len(present.child) == 0 and cnt == 0 :
            return 1
        elif cnt <= 0 : 
            return 0 
        for i in present.child.keys() :
            result += self.checkLeaf(present.child[i], cnt - 1, current)
        return result

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
                break
            if v in target.child :
                target = target.child[v]
            else :
                return 0

        result = self.checkLeaf(target, len(quer)-i, 0)
        return result
            

def solution(words, queries):
    answer = []
    a = Trie(words)
    a.makeFrontTrie()
    a.makeRearTrie()
    for i in queries :
        answer.append(a.getAnswer(i))
    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["fro??", "????o", "fr???", "fro???", "pro?"] ))