import sys
input = sys.stdin.readline

def soluction() :
    N = int(input())
    carNum = dict()
    numberOfCar = dict()
    outrunning = 0
    for i in range(N) :
        num = input().rstrip()
        carNum[num] = i 
        numberOfCar[i] = num
    for i in range(N) :
        num = input().rstrip()
        temp = carNum[num]
        for j in range(temp) :
            if j in numberOfCar :
                outrunning += 1
                break
        numberOfCar.pop(temp)

    return outrunning

if __name__ == "__main__":
    print(soluction())