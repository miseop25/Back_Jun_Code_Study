import sys
input=sys.stdin.readline

A, B, C = map(int, input().split(' '))
A_list = []
B_list = []
C_list = []
num_list = []

for i in range(A+B+C) :
    buf = int(input())
    if i < A :
        A_list.append(buf)
    elif i<(A+ B) :
        B_list.append(buf)
    elif i <(A+B+C) :
        C_list.append(buf)
    num_list.append(buf)


people_list = list(set(num_list))
ans_list = []
for i in people_list :
    cnt = 0
    if i in A_list :
        cnt +=1
    if i in B_list :
        cnt +=1
    if i in C_list :
        cnt +=1 
    if cnt >=2 :
        ans_list.append(i)
ans_list.sort()

print(len(ans_list))
for i in ans_list :
    print(i)

