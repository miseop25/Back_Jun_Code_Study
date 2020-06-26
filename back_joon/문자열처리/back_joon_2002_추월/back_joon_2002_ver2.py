import sys
input = sys.stdin.readline

def soluction(a) :
    f = open("/Users/minseopkim/Documents/test_data/tunnel/tunnel.in{0}".format(a), 'r')
    carNum = dict()
    numberOfCar = dict()
    N = int(f.readline())
    outrunning = 0
    for i in range(N) :
        num = f.readline().rstrip()
        carNum[num] = i 
        numberOfCar[i] = num
    for i in range(N) :
        num = f.readline().rstrip()
        temp = carNum[num]
        for j in range(temp) :
            if j in numberOfCar :
                outrunning += 1
                break
        numberOfCar.pop(temp)

    return outrunning

if __name__ == "__main__":
    for i in range(1, 10) :
        out = open("/Users/minseopkim/Documents/test_data/tunnel/tunnel.ou{0}".format(i), 'r').readline().rstrip()
        print(i, ":" ,soluction(i), "out : ", out)
