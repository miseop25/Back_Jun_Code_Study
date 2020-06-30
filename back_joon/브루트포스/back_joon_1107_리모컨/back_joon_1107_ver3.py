def soluction(N, nDict) :
    if N == 100 :
        return 0
    ansList = [abs(N- 100)]
    for i in range(1, 1000001) :
        temp = str(i)
        flag = True
        for k in temp :
            if int(k) not in nDict :
                flag = False
                break
        if flag :
            ansList.append(abs(N - i) + len(str(i)))
    return min(ansList)

    

if __name__ == "__main__":
    while True :
        N = int(input())
        num = [i for i in range(10)]
        M = int(input())
        if M != 0 :
            dosentWork = list(map(int, input().split(" ")))
            for i in dosentWork :
                num.remove(i)
        nDict = dict()
        for k in num :
            nDict[k] = True
        print(soluction(N, nDict))
        
        break
