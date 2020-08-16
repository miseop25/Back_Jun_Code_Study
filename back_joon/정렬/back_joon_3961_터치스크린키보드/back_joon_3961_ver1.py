import sys
input = sys.stdin.readline

class TouchScreen :
    def __init__(self) :
        self.keyboard = dict()
        self.top = "qwertyuiop"
        self.mid = "asdfghjkl"
        self.bot = "zxcvbnm"
    
    def initKeyboard(self) :
        for i, v in enumerate(self.top) : 
            self.keyboard[v] = (0, i)
        for i, v in enumerate(self.mid) :
            self.keyboard[v] = (1,i)
        for i, v in enumerate(self.bot) :
            self.keyboard[v] = (2, i)
    
    def checkDistence(self, a, b) :
        x = abs(self.keyboard[a][0] - self.keyboard[b][0])
        y = abs(self.keyboard[a][1] - self.keyboard[b][1])
        return x + y

        
    def soluction(self) :
        word, case = map(str, input().split(" "))
        result = []
        for _ in range(int(case)) :
            temp = input().rstrip()
            cnt = 0 
            for i in range(len(word)) :
                cnt += self.checkDistence(word[i], temp[i])
            result.append([temp, cnt])
        result = sorted(result, key= lambda x: (x[1], x[0] )  )
        for w, count in result :
            print(w, count)
            

    


if __name__ == "__main__":
    N = int(input())
    a = TouchScreen()
    a.initKeyboard()
    for _ in range(N) :
        a.soluction()
