import sys
input = sys.stdin.readline

k = int(input())
num = list(map(int, input().split(" ")))
len_num = len(num)
answer = []

for _ in range(k) :
    buf =[]

    for i in range(len(num)) :
        if i%2 != 1:
            answer.append(num[i])
            buf.append(num[i])
    
    for j in buf :
        num.remove(j)

for i in range(k) :
    str_buf = ""
    temp = []
    cnt = 0
    for j in range(2**(i)) :
        temp.append(answer.pop())
        
    for a in range(len(temp)) :
        if cnt == 0 :
            str_buf =str_buf+ str(temp.pop())
            cnt = -1
        else :
            str_buf =str_buf+ " " + str(temp.pop())
    
    print(str_buf)

    



