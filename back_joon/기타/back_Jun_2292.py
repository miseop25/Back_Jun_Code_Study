import sys

N = int(input())
first = 2
last = 7
count = 1

while N > 0 :
    if N == 1 :
        N = -1
        count = 0
    else : 
        if (N >= first and N <= last) : 
            N = -1
        else : 
            first = first +(count*6)
            last = last + ((count+1)*6)
            count = count + 1

count = count + 1
print(count)