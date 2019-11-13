N = int(input())


for i in range(N) :
    num_list = []
    answer = 0
    num_list = list(map(int, input().split(' ')))
    for k in num_list :
        if k%2 != 0 : 
            answer = answer + k 
    buf = '#' + str(i+1)
    print(buf, answer)
