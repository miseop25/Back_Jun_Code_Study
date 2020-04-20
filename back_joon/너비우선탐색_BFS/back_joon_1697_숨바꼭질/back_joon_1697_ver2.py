N , K = map(int, input().split(" "))

time = 0
cnt = 1
while N != K :
    time = 1
    ans_dict = {-1: [N-1], 1: [N+1],2:[N*2]}
    buf = []
    for i in ans_dict[-1] :
        if i > 0 :
            buf.append(i - 1)
        if i < K :
            buf.append(i*2)
    ans_dict[-1] = buf.copy()
    buf = []
    for j in ans_dict[1] :
        if j < K :
            buf.append(j+1)
            buf.append(j*2)
    ans_dict[1] = buf.copy()
    buf = []
    for q in ans_dict[2] :
        if i > 0 :
            buf.append(q-1)
        if i < K :
            buf.append(q+1)
            buf.append(q*2)
    ans_dict[2] = buf.copy()

    for check in ans_dict :
        if K in ans_dict[check] :
            cnt = - 1
            break
    if cnt == -1 :
        break
    time += 1
    




print(time)