import collections
N, K = map(int, input().split(" "))
cnt = 0
buf = [i for i in range(2, N+1)]
num = collections.deque(buf)
answer = 0
check = True
while check :
    num_buf = collections.deque([])
    if num : 
        p = num.popleft()
        cnt += 1
    else :
        break
    if cnt == K :
        check = False
        answer = p
        break
    for i in num :
        if (i % p) == 0 :
            cnt += 1
            if cnt == K :
                answer = i
                check = False
                break
        else :
            num_buf.append(i)
    num = num_buf.copy() 
print(answer)