import sys
import collections
input = sys.stdin.readline

def solucton() :
    time = 1 
    if len(craneDict[crane[-1]]) != M :
        return -1
    i = 0
    cnt = 0
    while True :
        if not craneDict[crane[i]] :
            if i == N-1 :
                i = -1
                time +=1
            i += 1
            continue

        if boxCounter[craneDict[crane[i]][0]] > 0 :
            boxCounter[craneDict[crane[i]][0]] -= 1
            cnt += 1
            craneDict[crane[i]].popleft()
        else :
            craneDict[crane[i]].popleft()
            continue
        if cnt == M :
            break
        if i == N-1 :
            i = -1
            time +=1
        i += 1

    return time

if __name__ == "__main__":
    N = int(input())
    crane = list(map(int, input().split(" ")))
    M = int(input())
    box = list(map(int, input().split(" ")))

    boxCounter = collections.Counter(box)
    craneDict = dict()
    for i in crane :
        craneDict[i] = []
        for j in box :
            if j <= i :
                craneDict[i].append(j)
        craneDict[i] = collections.deque(sorted(craneDict[i], key= lambda x : -x))


    crane = sorted(crane)
        
    print(solucton())


