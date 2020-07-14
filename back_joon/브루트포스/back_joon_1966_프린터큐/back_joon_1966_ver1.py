import sys
from collections import deque
input = sys.stdin.readline

def findMax(dq) :
    result = list(sorted(dq, key= lambda x: -x[1]))
    return result[0][1]

def soluction() :
    N, M = map(int, input().split(" "))
    temp = list(map(int, input().split(" ")))
    prList = deque([])
    for i, val in enumerate(temp) :
        prList.append([i, val])
    
    cnt = 0
    topVal = findMax(prList)
    while prList :
        temp = prList.popleft()
        if temp[1] == topVal :
            cnt += 1
            if temp[0] == M :   return cnt
            topVal = findMax(prList)
        else :
            prList.append(temp)
    return cnt
            

    

if __name__ == "__main__":
    case = int(input())
    for _ in range(case) :
        print(soluction())
