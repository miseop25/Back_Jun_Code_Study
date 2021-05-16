import sys
from collections import deque

class Soluction :
    def __init__(self, N,K):
        self.N = N
        self.K = K
        self.que = deque([i for i in range(1, N+1)])
        self.answer = []

    def getAnswer(self) :
        while self.que :
            for _ in range(self.K-1) :
                self.que.append(self.que.popleft())
            self.answer.append(str(self.que.popleft()))

        resultStr = "<" + ', '.join(self.answer) + ">"
        return resultStr


if __name__ == "__main__":
    N,K = map(int, input().split(" "))
    s= Soluction(N,K)
    print(s.getAnswer())

        