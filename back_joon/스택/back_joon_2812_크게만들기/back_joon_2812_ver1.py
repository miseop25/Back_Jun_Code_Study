import sys
input = sys.stdin.readline

def soluction(N,K, num) :
    numDict = dict()
    word = ''.join(num)
    for i in range(10) :
        numDict[i] = 0
    
    for i in num :
        numDict[int(i)] += 1
    
    for i in range(10) :
        if numDict[i] == 0:
            continue
        if K-numDict[i] >= 0 :
            word = word.replace(str(i),'', numDict[i])
            K -= numDict[i]
        else :
            word = word.replace(str(i),'',K )
            K = 0
        if K == 0:
            return word
    return word



if __name__ == "__main__":
    N, K = map(int, input().split(" "))
    num = list(input().rstrip())
    print(soluction(N,K,num))


