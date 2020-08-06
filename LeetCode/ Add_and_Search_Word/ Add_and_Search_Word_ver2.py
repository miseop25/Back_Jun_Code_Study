class WordDictionary:
    def __init__(self):
        self.wordDict = dict()        

    def addWord(self, word: str) -> None:
        width = len(word)
        if width in self.wordDict :
            self.wordDict[width].append(word)
        else :
            self.wordDict[width] = [word]


    def search(self, word: str) -> bool:

        comp = []
        for i, v in enumerate(word) :
            if v != "." :
                comp.append([i,v])
        if len(word) in self.wordDict :
            for i in self.wordDict[len(word)] :
                flag = True
                for j, v in comp :
                    if v == i[j] :
                        continue
                    else :
                        flag = False
                        break
                if flag :
                    return True
        return False
        


# Your WordDictionary object will be instantiated and called as such:
test = [["bad"],["dad"],["mad"],["pad"],["bad"]]
obj = WordDictionary()
for i in test : 
    obj.addWord(i[0])
print(obj.wordSet)

# param_2 = obj.search(word)