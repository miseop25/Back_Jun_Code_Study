import sys
import itertools
input = sys.stdin.readline


def find_array(N, K):
    ans = []
    num_list = []
    for i in range(N-K+1) :
        num_list.append(i+1)
    for j in num_list :
        cnt = 0
        temp = N
        buf = []
        buf.append(j)
        temp -= j
        cnt += 1
        while cnt != K :
            if temp-j <0 :
                
                pass
            else :
                temp = temp -j
                buf.append(temp)
                cnt +=1



    return ans


N, K = map(int, input().split(" "))
num = list(map(int, input().split(" ")))
answer = []

if N == K :
    print(0)
elif K == 1 :
    print(num[N-1] - num[0])
else :
    anslist = find_array(N, K)

