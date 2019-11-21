import sys
input=sys.stdin.readline

num_list = list(map(int, input().split(' ')))
buf_list = []
for i in range(1,7) :
    buf_list.append(i)
buf = num_list[0]
cnt= 0
cnt1 = 0
for i in num_list :
    try :
        buf_list.remove(i)
    except :
        pass



if len(buf_list) == 1 :
    if buf_list[0] == 1 or buf_list[0] == 2 or buf_list[0] == 6 or buf_list[0] == 5 :
        print('YES')
    else :
        print('NO')
elif len(buf_list) == 2 :
    if 1 in buf_list :
        if buf_list[1] ==2 or buf_list[1] == 6:
            print('YES')
        else :
            print('NO')
    elif 5 in buf_list :
        if buf_list[1] == 6 :
            print('YES')
        else :
            print('NO')
else :
    print('NO')

