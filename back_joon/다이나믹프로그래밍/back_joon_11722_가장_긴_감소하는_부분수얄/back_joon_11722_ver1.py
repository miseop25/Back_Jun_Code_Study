import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split(" ")))
dp = [1 for i in range(N)] 

for i in range(1, N) :
    buf = []
    for j in range(i) :
        if num[i] < num[j] :
            buf.append(dp[j])
    
    if buf :
        dp[i] += max(buf)
print(max(dp))