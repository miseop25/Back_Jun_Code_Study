import sys
import itertools
input = sys.stdin.readline


def soluction() :
    N, K = map(int, input().split(" "))
    ansList = []
    already = {'a': True, "n": True, "t": True, "i": True, "c": True, '': True}
    alpa = set()
    K = K - 5
    if K < 0 : return 0
    if K == 26 : return N

    words = []
    cnt = 0
    for _ in range(N) :
        buf = list(input().lstrip("anta").rstrip("tica\n"))
        buf = set(buf)
        if K == 0 :
            flag = True
            for i in buf :
                if i not in already :
                    flag = False
                    break
            if flag :
                cnt += 1
        else :
            words.append(buf)
            for i in buf :
                if i not in already :
                    alpa.add(i)
    if K == 0 :
        return cnt
    
    if K > len(alpa) :
        K = len(alpa)
    comb = list(itertools.combinations(alpa, K))

    for c in comb :
        bufDict = dict()
        for i in c :
            bufDict[i] = True
        cnt = 0
        for w in words :
            flag = True
            for i in w :
                if i in already : 
                    continue
                elif i in bufDict : 
                    continue
                else : 
                    flag = False
                    break
            if flag :
                cnt += 1
        ansList.append(cnt)
        
    
    return max(ansList)


print(soluction())
