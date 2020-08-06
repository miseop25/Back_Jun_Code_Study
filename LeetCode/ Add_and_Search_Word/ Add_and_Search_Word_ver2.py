import itertools
class WordDictionary:
    

    def __init__(self):
        self.wordSet = set()
        

    def addWord(self, word: str) -> None:
        self.wordSet.add(word)
        self.wordSet.add("."*len(word))
        for i in range(len(word)) :
            check = list(itertools.combinations([k for k in range(len(word))], i))
            for j in check :
                temp = list(word)
                for k in j :
                    temp[k] = "."
                self.wordSet.add("".join(temp))


        

    def search(self, word: str) -> bool:
        if word in self.wordSet :
            return True
        return False
        


# Your WordDictionary object will be instantiated and called as such:
test = [["bad"],["dad"],["mad"],["pad"],["bad"]]
obj = WordDictionary()
for i in test : 
    obj.addWord(i[0])
print(obj.wordSet)

# param_2 = obj.search(word)