import sys
import math
input = sys.stdin.readline

N = int(input())
answer = 0 

def get_ans(N, first_root) : 
    buf = N
    ans_list = []
    cnt = 0
    while True :
        if buf >0 :
            ans_list.append(first_root)
        elif buf == 0:
            ans_list.append(first_root)
            print(ans_list)
            return len(ans_list)
        first_root = math.sqrt(buf)
        first_root = math.floor(first_root)
        buf = buf - math.pow(first_root, 2)

        if cnt >= 3 :
            return -1
        else :
            cnt += 1

first_root = math.sqrt(N)
first_root = math.floor(first_root)
answer = []
root_list = []

for i in range(1, first_root+1) :
    root_list.append(i)

if root_list :
    for i in root_list :
        buf = N - math.pow(i,2)
        ans = get_ans(buf, i)
        if ans != -1 :
            answer.append(ans)
    print(min(answer))
else :
    print(1)

 