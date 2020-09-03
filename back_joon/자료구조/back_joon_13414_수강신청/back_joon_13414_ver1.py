import sys
input = sys.stdin.readline


if __name__ == "__main__":
    K, L = map(int, input().split(" ")) 
    waitingLine = dict()
    for i in range(L) :
        num = input().rstrip()
        if num in waitingLine :
            waitingLine[num] = i
        else :
            waitingLine[num] = i
    result = sorted(waitingLine.items(), key= lambda x:x[1])
    if K > len(waitingLine) :
        K = len(waitingLine)
    for i in range(K) :
        print(result[i][0])


