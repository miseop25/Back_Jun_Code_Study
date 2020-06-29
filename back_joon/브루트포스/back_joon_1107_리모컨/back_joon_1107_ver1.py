def soluction(N, num) :
    if N == 100 :
        return 0
    if len(num) == 0 :
        return abs(100 - N)
    ansList = [abs(N- 100)]
    nStr = str(N)
    cnt = 0
    st = ""
    for i in nStr :
        temp = sorted(num, key= lambda x: abs(x-int(i)))
        st += str(temp[0])
    cnt += len(str(int(st)))
    cnt += abs(N - int(st))
    ansList.append(cnt)


    return min(ansList)

if __name__ == "__main__":
    N = int(input())
    num = [i for i in range(10)]
    M = int(input())
    if M != 0 :
        dosentWork = list(map(int, input().split(" ")))
        for i in dosentWork :
            num.remove(i)
    print(soluction(N, num))
