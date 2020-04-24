import sys
input = sys.stdin.readline

def soluction():
    dp = [card[0]]
    if N > 1 :
        if card[0]*2 > card[1] :
            dp.append(card[0]*2)
        else :
            dp.append(card[1])
    else :
        return dp[0]
    
    for i in range(2, N) :
        buf = [card[i]]
        for j in range(i//2, i+1) :
            v, m = divmod(i+1, j)
            if m == 0 :
                buf.append(dp[j-1]* v)
            else :
                buf.append(dp[j-1]* v + dp[m-1])
        dp.append(max(buf))
    return dp[-1]


N = int(input())
card = list(map(int, input().split(" ")))
print(soluction())
    