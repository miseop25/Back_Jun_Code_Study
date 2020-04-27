import collections

def plus() :
    dp = collections.deque([0,1])
    if N <= 1 :
        print(dp[abs(N)])
    else :
        for _ in range(2, N+1) :
            dp.append(dp.popleft() + dp[0])
        print(dp[-1]%1000000000)

def minus() :
    dp = collections.deque([0, 1])
    if abs(N) <= 1 :
        print(dp[abs(N)])
    else :
        for _ in range(2, abs(N) +1) :
            dp.append(dp.popleft() - dp[0])
        print(abs(dp[-1])%1000000000)

N = int(input())

if N == 0 :
    print(0)
    print(0)
elif N > 0 :
    print(1)
    plus()
else :
    if abs(N)%2 == 0 :
        print(-1)
    else :
        print(1)
    minus()


