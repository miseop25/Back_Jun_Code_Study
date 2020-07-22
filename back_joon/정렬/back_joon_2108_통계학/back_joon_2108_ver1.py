import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    cntDict = dict()
    sums = 0
    num = []
    for _ in range(N) :
        a = int(input())
        if a in cntDict :
            cntDict[a] += 1
        else :
            cntDict[a] = 1
        sums += a
        num.append(a)
    
    num = sorted(num)
    cnt = sorted(cntDict.items(), key= lambda x: (-x[1], x[0]))
    answer = []
    answer.append(round(sums/N))
    answer.append(num[N//2])
    if len(cnt) > 1 :
        if cnt[0][1] == cnt[1][1] :
            answer.append(cnt[1][0])
        else :
            answer.append(cnt[0][0])
    
    if len(num) !=  1 :
        answer.append(num[-1] - num[0])
    else :
        answer.append(0)
    

    for i in answer :
        print(i)

    