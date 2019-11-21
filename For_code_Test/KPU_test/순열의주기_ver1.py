import sys
input=sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split(' ')))
buf_list = []
ans_list =[[]]
for i in range(1,N+1) :
    buf_list.append(i)

cnt = 0
ans_cnt = 0

while buf_list :
    try :
        ans_list[ans_cnt].append(cnt +1)
        buf_list.remove(cnt +1)
        cnt = num_list[cnt] - 1 
    except :
        ans_cnt +=1
        cnt = buf_list[0]-1
        ans_list.append([])

ans_list[ans_cnt].append(cnt +1)

print(len(ans_list))
for i in ans_list :
    buf_str = ''
    for j in range(len(i)) :
        buf_str += str(i[j])
        if j != len(i)-1 :
            buf_str += ' '
        else :
            break
    print(buf_str)
