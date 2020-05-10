import sys
input=sys.stdin.readline

N = int(input())

for _ in range(N):
    cnt = 0
    answer = 0
    buf = input()
    for i in buf :
        if i == "O":
            cnt += 1
            answer += cnt
        else :
            cnt = 0
    print(answer)