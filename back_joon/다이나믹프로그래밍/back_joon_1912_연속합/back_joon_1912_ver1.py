import sys
input = sys.stdin.readline

def soluction() :
    if N == 1 :
        return numList[0]
    answer = numList[0]
    dp = []

    for i in range(1, N) :
        dp.append(numList[i])
        if answer == None : 
            if numList[i] > 0 :
                answer = numList[i]  
            else : continue
        elif (answer + numList[i]) > 0 :
            dp.append(answer)
            answer += numList[i]
        else :
            dp.append(answer)
            answer = None
    if answer != None :
        dp.append(answer)
    return max(dp)

if __name__ == "__main__":
    N = int(input())
    numList = list(map(int, input().rstrip().split(" ")))
    print(soluction())
