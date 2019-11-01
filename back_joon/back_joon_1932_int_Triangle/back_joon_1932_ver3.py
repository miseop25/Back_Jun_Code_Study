
def sum_cal(prelist, afterlist) :
    ans_list = []
    num = len(prelist)
    for i in range(num) :
        if i == 0 :
            ans_list.append(prelist[i] + afterlist[i])
        if i >0 :
            first = prelist[i-1] + afterlist[i]
            second = prelist[i] + afterlist[i]
            if first > second :
                ans_list.append(first)
            else :
                ans_list.append(second)
                            
        if i == num-1 :
            ans_list.append(prelist[i] + afterlist[i+1])

    return ans_list

N = int(input())
prelist = list()
afterlist = list()

for i in range(N) : 
    if i == 0 :
        prelist = list(map(int , input().strip().split(' ')))
        afterlist = prelist
    else :
        afterlist = list(map(int , input().strip().split(' ')))
        prelist = sum_cal(prelist, afterlist)


print(max(prelist))


