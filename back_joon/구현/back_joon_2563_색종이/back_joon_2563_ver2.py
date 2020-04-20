import sys
import collections
input = sys.stdin.readline

N = int(input())
answer = N*100
paper = [[1 for i in range(100)] for j in range(100)]

for i in range(N):
    x,y  = map(int, input().split(" "))
    for i in range(x, x+10):
        for j in range(y, y+10) :
            paper[i][j] = 0
buf = 0
for i in paper :
    buf += sum(i)
print(10000- buf)
