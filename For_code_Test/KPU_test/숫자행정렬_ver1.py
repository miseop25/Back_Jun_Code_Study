import sys
from operator import itemgetter, attrgetter

N = int(input())

num = []
buf = []
len_num = []
for _ in range(N):
    buf = list(map(int, input().split(' ')))
    len_num.append(len(buf))
    num.append(buf)

sorted_num = sorted(num, key=itemgetter(0,1))

for i in sorted_num :
    buf_str = ''
    for a in range(len(i)-1):
        if i[a] != -1 :
            buf_str += str(i[a])
            buf_str += ' '
        else :
            break
    print(buf_str)
        

