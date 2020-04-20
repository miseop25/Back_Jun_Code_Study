def soluction(n) :
    dp = [1,3]
    if n < 3 :
        return dp[n-1]
    for i in range(2, n) :
        dp.append(dp[i-1] + dp[i-2]*2)
    return dp[-1]%10007

n = int(input())
print(soluction(n))