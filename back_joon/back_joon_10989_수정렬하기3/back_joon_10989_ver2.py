import sys
input = sys.stdin.readline

N = int(input())
num_dic = dict()

for _ in range(N) :
    temp = int(input())
    if temp in num_dic :
        num_dic[temp] += 1
    else :
        num_dic[temp] = 1
    
for i in sorted(num_dic.items()) :
    for j in range(i[1]) :
        print(i[0])


