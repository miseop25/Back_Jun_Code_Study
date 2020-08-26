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
        index = quer.find("?")
        flag = True
        result = 0
        # True 이면 접미사 찾아야함
        # False 이면 접두사 찾야아함
        if index == 0 :
            quer = quer[::-1]
            index = quer.find("?")
        else :
            flag = False
        
        if flag : 
            target = self.rear
        else :
            target = self.front

        for i in quer[: index] :
            if i in target.child :
                target = target.child[i]
            else :
                return 0

        result = self.checkLeaf(target, len(quer)-index, 0)
        return result
            

def solution(words, queries):
    answer = []
    a = Trie(words)
    a.makeFrontTrie()
    a.makeRearTrie()
    for i in queries :
        answer.append(a.getAnswer(i))
    return answer

print(solution(["frodo", "front", "front", "frozen", "frame", "kakao"],["?????", "????o", "fr???", "fro???", "pro?"] ))