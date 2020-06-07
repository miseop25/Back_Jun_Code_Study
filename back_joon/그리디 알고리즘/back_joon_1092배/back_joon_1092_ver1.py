import sys
import collections
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    crane = list(map(int, input().split(" ")))
    M = int(input())
    box = collections.deque(map(int, input().split(" ")))

    craneDict = dict()
    for i in crane :
        craneDict[i] = []

    box = collections.deque(sorted(box, key= lambda x: -x))    
    crane = sorted(crane, key= lambda x: -x)
    time = 1 
    cnt = -1
    check = M
    while box :
        cnt += 1
        if cnt == N :
            cnt = 0
            time += 1
            if check == len(box) :
                time = -1
                break
            else :
                check = len(box)

        if crane[cnt] >= box[0] :
            craneDict[crane[cnt]].append(box.popleft())
        elif crane[cnt] >= box[-1] :
            craneDict[crane[cnt]].append(box.pop())
        
    print(time)


