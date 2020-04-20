N , K = map(int, input().split(" "))

time = 0
if N != K :
    time = 1
    ans_list = [N-1, N+1, N*2]


    while K not in ans_list :
        buf = []
        for i in ans_list:
            buf.append(i-1)
            buf.append(i+1)
            buf.append(i*2)
        set_buf = set(buf)
        ans_list = list(set_buf)
        time += 1

print(time)