import sys
N = int(input())
series = [0] * 10001

for i in range(N):
    a = int(sys.stdin.readline())
    series[a] = series[a] + 1

for b in range(len(series)):
    if series[b] !=0:
        for c in range(series[b]):
            print(b)

#  출처 : https://kminito.github.io/baekjoon/2018/05/07/baekjoon_10989/