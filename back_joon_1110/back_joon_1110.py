N = int(input())

cnt = 1
new = N

while True :
    A = int(new/10)
    B = int(new%10)
    C = A + B
    new = (B*10) + (C%10)
    if new == N :
        break
    else :
        cnt = cnt + 1

print(cnt)