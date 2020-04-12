import collections

def soluction(n) :
    dp = collections.deque([1,3])
    if n < 3 :
        return dp[n-1]
    answer = 0
    for _ in range(2, n) :
        answer = dp.popleft()*2 + dp[0]
        dp.append(answer)
    return answer%10007

n = int(input())
print(soluction(n))