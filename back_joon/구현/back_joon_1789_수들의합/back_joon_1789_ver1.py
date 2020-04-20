import collections
S = int(input())

pow_num = int(pow(S, 0.5))
ans_list = collections.deque([i for i in range(1, pow_num+1)])
buf = sum(ans_list)

while True :

    if buf == S :
        break
    elif buf < S :
        pow_num += 1
        ans_list.append(pow_num)
        buf += pow_num
    else :
        check = buf - S 
        if check in ans_list :
            ans_list.remove(check)
            break
        else :
            minus = ans_list.popleft()
            buf -= minus
print(len(ans_list))