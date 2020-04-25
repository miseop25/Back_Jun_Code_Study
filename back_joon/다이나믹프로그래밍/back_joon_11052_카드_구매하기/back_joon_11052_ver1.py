import sys
input = sys.stdin.readline

def soluction():
    #  dp 저장소 생성, 2번째 값 까지 저장
    dp = [card[0]]
    if N > 1 :
        if card[0]*2 > card[1] :
            dp.append(card[0]*2)
        else :
            dp.append(card[1])
    else :
        return dp[0]
    
    #  각각의 수를 만들 수 있는 최대의 값 dp에 저장
    #  3장을 만들때의 최댓값, 4장, 5장 ...
    for i in range(2, N) :
        buf = [card[i]]
        for j in range((i+1)//2, i+1) :
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
    