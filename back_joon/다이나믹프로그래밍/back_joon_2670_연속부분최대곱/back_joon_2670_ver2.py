import sys
input = sys.stdin.readline

def soluction(N) :
    dp = [0 for _ in range(N)] 
    dp[0] = float(input())
    for i in range(1, N) :
        num = float(input())
        if dp[i-1] >= 1 :
            dp[i] = dp[i-1]*num
        else :
            dp[i] = num
    answer = max(dp)
    return answer




if __name__ == "__main__":
    N = int(input())
    ans = soluction(N)
    print("%.3f" %ans)