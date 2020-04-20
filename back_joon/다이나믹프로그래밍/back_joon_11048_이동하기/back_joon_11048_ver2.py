import sys
import collections
input = sys.stdin.readline

N, M = map(int, input().split(" "))
dp = [[0 for i in range(M)] for j in range(N)]
candy_map = []
for i in range(N) :
    candy_map.append(list(map(int, input().split(" "))))

for i in range(N) :
    for j in range(M) :
        buf = [candy_map[i][j]]
        if i - 1  >= 0  and j-1 >= 0 :
            buf.append(dp[i-1][j-1] + candy_map[i][j])
        if i >= 0 and j-1 >= 0 : 
            buf.append(dp[i][j-1] + candy_map[i][j])
        if i-1 >= 0 and j >= 0 :
            buf.append(dp[i-1][j] + candy_map[i][j])
        dp[i][j] = max(buf)

print(dp[-1][-1])