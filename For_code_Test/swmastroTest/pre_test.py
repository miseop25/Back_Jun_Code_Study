import sys
input = sys.stdin.readline

N, K = map(int, input().split(" "))
num_list = list(map(int, input().split(" ")))

one_index = num_list.index(1) + 1
ans_list = []
if one_index > K :
    buf_index = one_index-1
    for i in range(one_index) :
        after_len = N-one_index-i +1
        before_len = N -after_len -1

        af_value, af_tmep = divmod(after_len, K-1)
        if af_tmep != 0 :
            af_value +=1
        
        bef_value, bef_temp = divmod(before_len, K-1)
        if bef_temp != 0 :
            bef_value += 1

        ans = af_value + bef_value
        ans_list.append(ans)


else :
    value , temp = divmod(N, K-1)
    if temp != 0 :
        value += 1 
    ans_list.append(value)


print(min(ans_list))
