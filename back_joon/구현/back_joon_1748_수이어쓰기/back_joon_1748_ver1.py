N = int(input())+1

check = 10
cnt = 1
answer = 0

for i in range(1, N) :
    if i < check :
        answer += cnt
    else :
        check *= 10 
        cnt += 1
        answer += cnt

print(answer)