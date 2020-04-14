import sys
import copy
input = sys.stdin.readline

def soluction(sk, width) :
    if width == 1 :
        return max(sk[0][0], sk[1][0])
    elif width == 2 :
        return max((sk[0][0] + sk[1][1]), (sk[0][1] + sk[1][0]))

    dp = [[0 for j in range(width)] for i in range(2)]
    dp[0][0] = sk[0][0]
    dp[1][0] = sk[1][0]
    dp[0][1] = sk[0][1] + sk[1][0]
    dp[1][1] = sk[1][1] + sk[0][0]
    for i in range(2, width) :
        dp[0][i] = sk[0][i] + max(dp[1][i-1], dp[1][i-2])
        dp[1][i] = sk[1][i] + max(dp[0][i-1], dp[0][i-2])
    return max(dp[1][width-1], dp[0][width -1])





T = int(input())
for _ in range(T) :
    sticker = []
    ans_list = []
    n = int(input())
    for i in range(2) :
        buf = list(map(int, input().split(" ")))
        sticker.append(buf)   
    print(soluction(sticker, n))
    