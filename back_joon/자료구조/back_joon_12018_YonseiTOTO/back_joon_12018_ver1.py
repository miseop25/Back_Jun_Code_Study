import sys
input = sys.stdin.readline


class Soluction :
    def __init__(self):
        self.N = 0
        self.M = 0
        self.answer = 0
        self.course = []
    
    def firstInput(self) :
        n,m = map(int, input().rstrip().split(" "))
        self.N = n
        self.M = m
        for _ in range(n) :
            self.courseInput()

    def courseInput(self) :
        person, total = map(int, input().rstrip().split(" "))
        arr = list(map(int, input().split(" ")))
        arr = sorted(arr, key = lambda x: -x)
        if person < total :
            self.course.append(1)
        else :
            self.course.append(arr[total-1])
    
    def getAnswer(self) :
        self.course = sorted(self.course)
        for i in self.course :
            if self.M - i >= 0 :
                self.answer += 1 
                self.M -= i
            else :
                break
        return self.answer

if __name__ == "__main__":
    s = Soluction()
    s.firstInput()
    answer = s.getAnswer()
    print(answer)

