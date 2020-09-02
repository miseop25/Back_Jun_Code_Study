import sys
from collections import deque
input = sys.stdin.readline


def topologySort(inDegree, numDict) :
    que = deque([])
    result = []
    for i, v in enumerate(inDegree) :
        if v == 0 :
            que.append(i)
            inDegree[i] = -1

    
    for i in range(len(inDegree)-1) :
        que = deque(sorted(que))
        if len(que) == 0 :
            return -1
        temp = que.popleft()
        result.append(str(temp))
        if temp not in numDict :
            continue
        for j in numDict[temp] :
            if inDegree[j]-1 >= 0 :
                inDegree[j] -= 1
                if inDegree[j] == 0 :
                    que.append(j)
        
    return result

if __name__ == "__main__":
    N, M = map(int, input().split(" ")) 
    
    inDegree = [0 for _ in range(N+1)]
    inDegree[0] = -1
    numDict = dict()

    for _ in range(M) :
        a, b = map(int, input().split(" "))
        inDegree[b] += 1
        if b in numDict:
            numDict[a].append(b)
        else : 
            numDict[a] = [b]
    result = topologySort(inDegree, numDict)
    print(' '.join(result))






    

