import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

class Soluction :
    def __init__(self, num) :
        self.cnt = 0
        self.answer = self.changeNum(num)

    def changeNum(self, num) :
        if num < 10 :
            return num
        else :
            temp = 0
            self.cnt += 1
            for i in str(num) :
                temp += int(i)
            return self.changeNum(temp)

    def printAnswer(self) :
        print(self.cnt)
        if self.answer%3 == 0 :
            print("YES")
        else :
            print("NO")

if __name__ == "__main__":
    N = int(input())
    s = Soluction(N)
    s.printAnswer()