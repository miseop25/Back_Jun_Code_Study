import sys
input=sys.stdin.readline


n = int(input())
first_num = int(input())
buf_list = []
buf_list.append([first_num, 1])
buf_list.append([0,0])


for k in range(n-1) :
    num = int(input())
    for i in range(len(buf_list)) :
        if buf_list[i][1] == 0 :
            buf_list[i][0] += num
            buf_list[i][1] += 1 
        elif buf_list[i][1] == 1 :
            buf_list.append([buf_list[i][0], 0])
            buf_list[i][0] += num
            buf_list[i][1] += 1
        else :
            buf_list[i][1] = 0

buf_list = sorted(buf_list, key=lambda x: x[0], reverse= True)
print(buf_list[0][0])
