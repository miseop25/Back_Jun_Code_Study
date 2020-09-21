import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


class Soluction :
    def __init__(self, array, C) :
        self.C = C 
        self.array = array
        self.answer = 0
    
    def binarySearch(self, left, right) :
        while left <= right :

            mid = (left + right)//2
            cnt = self.countNum(mid)
            if cnt >= C :
                self.answer = max(self.answer, mid)
                left = mid + 1
            else :
                right = mid -1
    
    def countNum(self, mid) :
        t = 0
        cnt = 1
        for i, v in enumerate(self.array) :
            if v >= self.array[t] + mid :
                t = i
                cnt += 1
        return cnt
    
    def getAnswer(self) :
        self.binarySearch(1, (self.array[-1] + self.array[0])//(C-1) + 1)
        print(self.answer)


if __name__ == "__main__":
    N, C = map(int, input().split(" "))
    array = [int(input()) for _ in range(N)]
    array = sorted(array)
    a = Soluction(array, C)
    a.getAnswer()
    