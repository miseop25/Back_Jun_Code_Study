import sys
import time
import math
class sol :
    def __init__(self):
        a, r, n, mods = map(int, input().rstrip().split(" "))
        self.cnt = 0
        self.st = time.time()
        t = self.fPow2(r,n)
        # t = math.pow(r,n)
        print(time.time() - self.st)
        ta = int(a *(t-1))
        root = r -1

        sumN = ta // root
        self.answer = int(sumN % mods)

    def fPow(self,C, n) :
        res = 1
        while n :
            if n & 1:
                res *= int(C)
            C *= int(C)
            n = n >> 1

        return res
    
    def fPow2(self, c, n) :
        if(n == 0) :
            return 1
        res = self.fPow2(c,n//2)
        if (n & 1) :
            return res * res * c
        else :
            return res * res






s = sol()
answer =  s.answer
cnt = s.cnt

print(answer)
