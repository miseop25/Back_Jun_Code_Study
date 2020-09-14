import sys
input = sys.stdin.readline

def soluction(N,M, vip) :
    dp = [1 for _ in range(N+1)]
    answer = 1
    if N > 2 :
        dp[1] = 1
        dp[2] = 2
    else :
        if N == 1 :
            return 1
        else :
            if vip :
                return 1
            else : return 2
    
    for i in range(3, N+1) :
        dp[i] = dp[i-1] + dp[i-2]
    
    if not vip :
        return dp[N]
    vip = sorted(vip)
    answer *= dp[vip[0]-1]
    st = vip[0] + 1
    for i in range(1, M) :
        answer *= dp[vip[i]-st]
        st = vip[i] + 1
    answer *= dp[N - st + 1]
    return answer



if __name__ == "__main__":
    N = int(input())
    M = int(input())
    vip = []
    for _ in range(M) :
        vip.append(int(input()))
    print(soluction(N,M,vip))

    
