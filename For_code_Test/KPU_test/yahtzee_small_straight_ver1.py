import sys
input=sys.stdin.readline

num_list = list(map(int, input().split(' ')))

buf = num_list[0]
cnt= 0
cnt1 = 0
for i in num_list[1:] :
    if (buf+1) == i :
        cnt +=1
    elif buf != i :
        cnt = 0
    if (buf-1) == i :
        cnt1 +=1 
    elif buf != i :
        cnt1 = 0
    buf = i

    if cnt>=3 or cnt1>=3 :
        break



if cnt >=3 or cnt1 >=3 :
    print('YES')
else :
    print('NO')
