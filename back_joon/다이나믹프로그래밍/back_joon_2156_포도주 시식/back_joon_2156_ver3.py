import sys
input=sys.stdin.readline


n = int(input())
buf_list = []
ans_list = [0,0,0]

for k in range(1, n+1) :
    num = int(input())
    buf_list.append(num)
    if k % 3 == 0  :
        ans_list[0] += buf_list[0] + buf_list[1]
        ans_list[1] += buf_list[1] + buf_list[2]
        ans_list[2] += buf_list[0] + buf_list[2]
        buf_list = []

if buf_list :
    l_buf = len(buf_list)
    if l_buf == 1 :
        ans_list[0] += buf_list[0]
        ans_list[2] += buf_list[0]
    if l_buf == 2 :
        ans_list[0] += buf_list[0] + buf_list[1]
        ans_list[1] += buf_list[1]

print(max(ans_list))
