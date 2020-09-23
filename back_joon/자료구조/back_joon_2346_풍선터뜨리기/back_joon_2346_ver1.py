import sys
from collections import deque
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def soluction(N, num) :
    check = [True for _ in range(N)]
    answer = []

    i = 0 
    cnt = 1
    cmd = num[0]
    answer.append(str(i+1))
    check[0] = False

    while cnt != N :
        i += cmd 

        if i > N-1 :
            v, r = divmod(i,N)
            i = r
        elif i < 0 :
            v, r = divmod(abs(i), N)
            i = N - r

        while not check[i] :
            if cmd <0 :
                i -= 1
            else :
                i += 1
            if i > N-1 :
                i -= N
            elif i < 0 :
                i = N-1
        answer.append(str(i+1))
        cnt += 1
        check[i] = False
        cmd = num[i]

    return ' '.join(answer)    
        


if __name__ == "__main__":
    N = int(input())
    num = list(map(int, input().split(" ")))
    print(soluction(N, num))
