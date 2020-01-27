import collections

def soluction(st_fn,dp_fn) :
    re_stack = collections.deque()

    buf = dp_fn[1] - dp_fn[0]
    re_stack.append(buf)

    answer = dp_fn[1] + buf

    for i in st_fn :
        buf = buf -i
        re_stack.append(buf)
        answer += buf
    
    return answer, re_stack

    


N = int(input())
dp = collections.deque([10,55])
stack_list = collections.deque([9,8,7,6,5,4,3,2])

cnt = 2
ans = 0


if N >2 :
    while cnt != N :
        ans, stack_list = soluction(stack_list, dp)
        dp.popleft()
        dp.append(ans)
        cnt +=1
    print(dp[1]%10007)



else :
    print(dp[N-1])