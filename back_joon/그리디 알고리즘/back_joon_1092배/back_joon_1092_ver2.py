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
        # 해당 크레인이 올길 수 있는 상자가 없을 경우
        if not craneDict[crane[i]] :
            if i == N-1 :
                i = -1
                time +=1
            i += 1
            continue
        # 크레인이 옮길 수 있는 최대 무게의 집이 box에 남아있는지 확인
        if boxCounter[craneDict[crane[i]][0]] > 0 :
            boxCounter[craneDict[crane[i]][0]] -= 1
            cnt += 1
            craneDict[crane[i]].popleft()
        #  box에 없다면 옮길 수 있는 최대 무게의 짐 pop
        else :
            craneDict[crane[i]].popleft()
            continue
        # 짐을 옮긴 횟수가 box의 수와 같다면 break
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

    # box의 개수를 각각 세서 몇개가 있는지 파악한다. 
    boxCounter = collections.Counter(box)
    craneDict = dict()
    #  각각의 크레인이 옮길 수 있는 짐들을 dict에 적재한다.
    for i in crane :
        craneDict[i] = []
        for j in box :
            if j <= i :
                craneDict[i].append(j)
        craneDict[i] = collections.deque(sorted(craneDict[i], key= lambda x : -x))

    crane = sorted(crane)
    print(solucton())


