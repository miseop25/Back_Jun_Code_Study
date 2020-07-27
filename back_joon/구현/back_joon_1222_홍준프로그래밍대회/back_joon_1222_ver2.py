import sys
input = sys.stdin.readline

numDict = dict()

def getDivisor(num) :
    for i in range(1, int(num**0.5) + 1) :
        if num%i == 0 :
            if i in numDict :
                numDict[i] += 1
            else :
                numDict[i] = 1
            temp = num//i
            if i != temp :
                if temp in numDict :
                    numDict[temp] += 1
                else : 
                    numDict[temp] = 1


if __name__ == "__main__":
    N = int(input())
    person = list(map(int, input().rstrip().split(" ")))
    for i in person :
        getDivisor(i)
    

    answer = sorted(numDict.items(), key= lambda x: -(x[0]*x[1]))
    for i in answer :
        if i[1] >= 2 :
            print(i[0]*i[1])
            break

