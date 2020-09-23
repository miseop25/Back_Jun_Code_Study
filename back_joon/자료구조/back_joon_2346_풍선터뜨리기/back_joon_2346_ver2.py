import sys
from collections import deque
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def soluction(N, num) :
    answer = []
    numDict = dict()
    que = deque([])
    for i in range(N) :
        numDict[i] = num[i]
        que.append(i)
    
    while que :
        target = que.popleft()
        cmd = numDict[target]
        answer.append(str(target+1))
        if not que :
            return ' '.join(answer)
        if cmd > 0 :
            for _ in range(cmd-1) :
                que.append(que.popleft())
        else :
            for _ in range(abs(cmd)) :
                que.appendleft(que.pop())
        
    return ' '.join(answer)    
        


if __name__ == "__main__":
    N = int(input())
    num = list(map(int, input().split(" ")))
    print(soluction(N, num))
