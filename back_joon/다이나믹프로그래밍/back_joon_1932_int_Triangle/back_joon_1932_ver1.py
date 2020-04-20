import itertools

N = int(input())
cases = list()
ans_list = list()
for i in range(N) :
    cases.append([])
    cases[i].extend(list(map(int , input().strip().split(' '))))

for i in range(N) :
    ans_list.append([])
    if i == 0 :
        ans_list[i].append([])
        ans_list[i][0].append(cases[i][0])
    else :
        for j in range(0,  len(ans_list[i-1])) :
            ans_list[i].append([])
            for k in ans_list[i-1][j] :
                ans_list[i][j].append(k + cases[i][j] )
                try :
                    ans_list[i].append([]) 
                    ans_list[i][j+1].append(k + cases[i][j+1])
                except :
                    pass

answer = list(itertools.chain(*ans_list[N-1]))

print(max(answer))


