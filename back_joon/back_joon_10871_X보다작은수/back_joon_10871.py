import sys
input = sys.stdin.readline

N , X = map(int, input().split(" "))
num = list(map(int, input().split(" ")))
answer = []
for i in num :
    if i < X :
        answer.append(str(i))

print(' '.join(answer))