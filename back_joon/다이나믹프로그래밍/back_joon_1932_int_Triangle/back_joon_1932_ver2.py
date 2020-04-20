import itertools

def sum_cal(prelist, afterlist) :
    ans_list = []
    ans_list.append([])
    cnt = 1
    for i in range(len(prelist)) :
        for k in prelist[i] :
            ans_list[i].append(k + afterlist[i])
            try :
                if cnt == 1 :
                    ans_list.append([])
                    cnt = -1
                ans_list[i+1].append(k + afterlist[i+1])
            except :
                pass
        cnt =1
    return ans_list

N = int(input())
prelist = list()
afterlist = list()

for i in range(N) : 
    if i == 0 :
        prelist.append([])
        prelist[0] = list(map(int , input().strip().split(' ')))
        afterlist = prelist[0]
    else :
        afterlist = list(map(int , input().strip().split(' ')))
        prelist = sum_cal( prelist, afterlist)


answer = list(itertools.chain(*prelist))
print(max(answer))


