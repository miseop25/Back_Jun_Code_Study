def solution(n) :
    dp = [1,2] 
    if n < 3 : 
        return dp[n-1]

    for i in range(2, n) :
        dp.append((dp[i-2] + dp[i-1])%1000000007)

    return dp[i]
    