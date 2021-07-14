import sys
input = sys.stdin.readline

class ReverseWord :
    def __init__(self):
        self.word = []
    
    def reVerseWord(self) :
        self.word = list(input().rstrip().split(" ")) 
        result = ''
        for w in self.word :
            result += w[len(w)::-1] + ' '
        result = result[:-1]
        print(result)

if __name__ == "__main__" :
    n = int(input()) 
    for _ in range(n) :
        s = ReverseWord() 
        s.reVerseWord()